/* tslint:disable */
/* eslint-disable */
// @generated
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL query operation: GetAllTag
// ====================================================

export interface GetAllTag_GetAllTag_tags {
  __typename: "Tag";
  tagName: string;
  id: number;
}

export interface GetAllTag_GetAllTag {
  __typename: "GetAllTagResponse";
  ok: boolean;
  error: string | null;
  tags: (GetAllTag_GetAllTag_tags | null)[] | null;
}

export interface GetAllTag {
  GetAllTag: GetAllTag_GetAllTag;
}
