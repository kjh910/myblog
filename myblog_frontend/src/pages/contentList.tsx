import { gql, useQuery } from "@apollo/client";
import { request } from "https";
import React, { Fragment, useState } from "react";
import { useParams } from "react-router";
import { GetAllContents, GetAllContentsVariables } from "../__generated__/GetAllContents";
import { Detail } from "./detail";
import { BrowserRouter as Router, Link } from "react-router-dom";

const GET_ALL_CONTENT = gql`
    query GetAllContents($tagId: Int){
        GetAllContents(tagId:$tagId){
            ok
            error
            contents{
                id
                content
                tagId
                tag{
                    id
                    tagName
                }
            }
        }
    }
`;

export const ContentList = () => {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const tagId = Number(urlParams.get('tagId'));
    const {data} = useQuery<GetAllContents, GetAllContentsVariables>(GET_ALL_CONTENT, {
        variables: {
            tagId:tagId
        }
    });
    return (
        <div className="container w-full md:max-w-3xl mx-auto pt-20">
            <div className="pb-4 border-b-2 border-solid border-gray-100">
                <h2 className="mb-7">
                    <b>전체 글</b>
                </h2>
                    {data?.GetAllContents.contents?.map(contents => (
                        <div className="flex flex-row-reverse justify-between mb-7">
                            <>
                                <div className="w-40 h-24 ml-10">
                                    {contents?.id}
                                </div>
                                <>
                                <div className="w-full pt-1">
                                    <Link to="/detail" className="hover:opacity-75">
                                        {contents?.content}
                                    </Link>
                                    <div className="mr-3 text-xs text-gray-800">
                                        {contents?.tag.tagName}
                                    </div>
                                </div>
                                </>
                            </>
                        </div>
                    ))} 
            </div>
        </div>
    );
}