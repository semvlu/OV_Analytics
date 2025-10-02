import * as fs from "fs";
import { fileURLToPath } from "url";
import * as path from "path";

import dotenv from "dotenv";
dotenv.config();

import { ApolloServer } from "@apollo/server";
import { startStandaloneServer } from "@apollo/server/standalone";
import { createClient } from "@clickhouse/client";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const typeDefs = fs.readFileSync(path.join(__dirname, "ov.gql"), "utf8");
import resolvers from "./resolvers.js";

const client = createClient({
  url: String(process.env.CLICKHOUSE_HOST),
  username: process.env.CLICKHOUSE_USER || "default",
  password: process.env.CLICKHOUSE_PASSWORD || "",
  database: process.env.CLICKHOUSE_DB || "default",
});

const server = new ApolloServer({
  typeDefs,
  resolvers,

  /* Older version: apollo-server
    formatResponse: (res: GraphQLResponse, requestContext: GraphQLRequestContext<any>) => {
        // Bug fixed: header: Content-Type: text/html
        // Set Content-Type header: application/json
        requestContext.response.http.headers.set('Content-Type', 'application/json');
        return res;
    }
  */
});

const startServer = async () => {
  try {
    await client.ping();
    // mongoose.connect(MONGODB);
    console.log("Connected to ClickHouse");

    // Start the Apollo server
    const { url } = await startStandaloneServer(server, {
      listen: { port: 5000 },
      context: async () => ({ client }),
    });
    console.log(`Server is running on ${url}`);
  } catch (err) {
    console.error(err);
    process.exit(1);
  }
};
startServer();

export { client };
