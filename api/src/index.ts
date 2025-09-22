import * as fs from "fs";
import * as path from "path";

import { ApolloServer } from "@apollo/server";
import { startStandaloneServer } from "@apollo/server/standalone";
import { createClient } from "@clickhouse/client";

const typeDefs = fs.readFileSync(path.join(__dirname, "ov.gql"), "utf8");
import resolvers from "./resolvers.js";

const client = createClient({
  url: String(process.env.CLICKHOUSE_HOST),
  username: String(process.env.CLICKHOUSE_USER),
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
