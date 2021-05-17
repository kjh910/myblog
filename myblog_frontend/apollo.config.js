module.exports = {
    client: {
      includes: ["./src/**/*.tsx"],
      tagName: "gql",
      service: {
        name: "myblog_backend",
        url: "http://localhost:4000/graphql",
      },
    },
  };