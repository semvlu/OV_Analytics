declare const resolvers: {
    Query: {
        bus(_: object, { ID }: {
            ID: string;
        }): Promise<unknown[]>;
        getBuses(_: object, { amount }: {
            amount: number;
        }): Promise<unknown[]>;
    };
};
export default resolvers;
//# sourceMappingURL=resolvers.d.ts.map