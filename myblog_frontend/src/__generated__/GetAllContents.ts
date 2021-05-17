/* tslint:disable */
/* eslint-disable */
// @generated
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL query operation: GetAllContents
// ====================================================

export interface GetAllContents_GetAllContents_contents_tag {
  __typename: "Tag";
  id: number;
  tagName: string;
}

export interface GetAllContents_GetAllContents_contents {
  __typename: "Content";
  id: number;
  content: string;
  tagId: number;
  tag: GetAllContents_GetAllContents_contents_tag;
}

export interface GetAllContents_GetAllContents {
  __typename: "GetAllContentsResponse";
  ok: boolean;
  error: string | null;
  contents: (GetAllContents_GetAllContents_contents | null)[] | null;
}

export interface GetAllContents {
  GetAllContents: GetAllContents_GetAllContents;
}

export interface GetAllContentsVariables {
  tagId?: number | null;
}
