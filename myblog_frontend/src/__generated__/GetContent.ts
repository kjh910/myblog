/* tslint:disable */
/* eslint-disable */
// @generated
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL query operation: GetContent
// ====================================================

export interface GetContent_GetContent_content_tag {
  __typename: "Tag";
  id: number;
  tagName: string;
}

export interface GetContent_GetContent_content {
  __typename: "Content";
  id: number;
  content: string;
  tag: GetContent_GetContent_content_tag;
}

export interface GetContent_GetContent {
  __typename: "GetContentResponse";
  ok: boolean;
  error: string | null;
  content: GetContent_GetContent_content | null;
}

export interface GetContent {
  GetContent: GetContent_GetContent;
}

export interface GetContentVariables {
  contentId: number;
  tagId: number;
}
