import { client } from "./index.js";

const resolvers = {
  Query: {
    async bus(_: object, { journey }: { journey: number }) {
      const result = await client.query({
        query: `
        SELECT * 
        FROM buses 
        WHERE journeynumber = '${journey}'
        `,
        format: "JSONEachRow",
      });
      return await result.json();
    },

    async getBuses(_: object, { amount }: { amount: number }) {
      const result = await client.query({
        query: `SELECT * FROM buses LIMIT ${amount}`,
        format: "JSONEachRow",
      });
      return await result.json();
    },
  },
};
export default resolvers;
