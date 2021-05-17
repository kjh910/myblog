export const typeDefs = ["type CreateContentResponse {\n  ok: Boolean!\n  error: String\n}\n\ntype Mutation {\n  CreateContent(tagId: Int!, content: String!): CreateContentResponse\n  DeleteContent(tagId: Int!, contentId: Int!): DeleteContentResponse\n  UpdateContent(contentId: Int!, tagId: Int!, content: String!): UpdateContentResponse\n  CreateTag(tagName: String!): CreateTagResponse\n  DeleteTag(tagId: Int!): DeleteTagResponse\n  UpdateTag(tagId: Int!, tagName: String!): UpdateTagResponse\n}\n\ntype DeleteContentResponse {\n  ok: Boolean!\n  error: String\n}\n\ntype GetAllContentsResponse {\n  ok: Boolean!\n  error: String\n  contents: [Content]\n}\n\ntype Query {\n  GetAllContents(tagId: Int): GetAllContentsResponse!\n  GetContent(tagId: Int!, contentId: Int!): GetContentResponse!\n  GetAllTag: GetAllTagResponse!\n  GetTag(tagId: Int!): GetTagResponse!\n}\n\ntype GetContentResponse {\n  ok: Boolean!\n  error: String\n  content: Content\n}\n\ntype Content {\n  id: Int!\n  content: String!\n  tagId: Int!\n  tag: Tag!\n  createdAt: String!\n  updatedAt: String\n}\n\ntype UpdateContentResponse {\n  ok: Boolean!\n  error: String\n}\n\ntype CreateTagResponse {\n  ok: Boolean!\n  error: String\n}\n\ntype DeleteTagResponse {\n  ok: Boolean!\n  error: String\n}\n\ntype GetAllTagResponse {\n  ok: Boolean!\n  error: String\n  tags: [Tag]\n}\n\ntype GetTagResponse {\n  ok: Boolean!\n  error: String\n  tag: Tag\n}\n\ntype Tag {\n  id: Int!\n  tagName: String!\n  contents: [Content]\n  createdAt: String!\n  updatedAt: String\n}\n\ntype UpdateTagResponse {\n  ok: Boolean!\n  error: String\n}\n"];
/* tslint:disable */

export interface Query {
  GetAllContents: GetAllContentsResponse;
  GetContent: GetContentResponse;
  GetAllTag: GetAllTagResponse;
  GetTag: GetTagResponse;
}

export interface GetAllContentsQueryArgs {
  tagId: number | null;
}

export interface GetContentQueryArgs {
  tagId: number;
  contentId: number;
}

export interface GetTagQueryArgs {
  tagId: number;
}

export interface GetAllContentsResponse {
  ok: boolean;
  error: string | null;
  contents: Array<Content> | null;
}

export interface Content {
  id: number;
  content: string;
  tagId: number;
  tag: Tag;
  createdAt: string;
  updatedAt: string | null;
}

export interface Tag {
  id: number;
  tagName: string;
  contents: Array<Content> | null;
  createdAt: string;
  updatedAt: string | null;
}

export interface GetContentResponse {
  ok: boolean;
  error: string | null;
  content: Content | null;
}

export interface GetAllTagResponse {
  ok: boolean;
  error: string | null;
  tags: Array<Tag> | null;
}

export interface GetTagResponse {
  ok: boolean;
  error: string | null;
  tag: Tag | null;
}

export interface Mutation {
  CreateContent: CreateContentResponse | null;
  DeleteContent: DeleteContentResponse | null;
  UpdateContent: UpdateContentResponse | null;
  CreateTag: CreateTagResponse | null;
  DeleteTag: DeleteTagResponse | null;
  UpdateTag: UpdateTagResponse | null;
}

export interface CreateContentMutationArgs {
  tagId: number;
  content: string;
}

export interface DeleteContentMutationArgs {
  tagId: number;
  contentId: number;
}

export interface UpdateContentMutationArgs {
  contentId: number;
  tagId: number;
  content: string;
}

export interface CreateTagMutationArgs {
  tagName: string;
}

export interface DeleteTagMutationArgs {
  tagId: number;
}

export interface UpdateTagMutationArgs {
  tagId: number;
  tagName: string;
}

export interface CreateContentResponse {
  ok: boolean;
  error: string | null;
}

export interface DeleteContentResponse {
  ok: boolean;
  error: string | null;
}

export interface UpdateContentResponse {
  ok: boolean;
  error: string | null;
}

export interface CreateTagResponse {
  ok: boolean;
  error: string | null;
}

export interface DeleteTagResponse {
  ok: boolean;
  error: string | null;
}

export interface UpdateTagResponse {
  ok: boolean;
  error: string | null;
}
