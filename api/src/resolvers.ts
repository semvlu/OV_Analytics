import { client } from "./index.js";

const resolvers = {
  Query: {
    async bus(_: object, { ID }: { ID: string }) {
      const result = await client.query({
        query: `SELECT * FROM bus WHERE id='${ID}'`,
        format: "JSONEachRow",
      });
      return await result.json();
    },

    async getBuses(_: object, { amount }: { amount: number }) {
      const result = await client.query({
        query: `SELECT * FROM bus LIMIT ${amount}`,
        format: "JSONEachRow",
      });
      return await result.json();
    },
  },
};
export default resolvers;
