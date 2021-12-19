import { gql, useQuery } from "@apollo/client";
import { GetContent, GetContentVariables } from "../__generated__/GetContent";
import React from "react";

const GET_CONTENT = gql`
    query GetContent($contentId: Int!, $tagId: Int!){
        GetContent(contentId:$contentId, tagId:$tagId){
            ok
            error
            content{
                id
                content
                tag{
                    id
                    tagName
                }
            }
        }
    }
`;

// export const Detail = () => (
//     <div>111</div>
// )
export const Detail = () => {
    // const queryString = window.location.search;
    // const urlParams = new URLSearchParams(queryString);
    // const tagId = Number(urlParams.get('tagId'));
    // const contentId = Number(urlParams.get('contentId'));

    // const {data} = useQuery<GetContent, GetContentVariables>(GET_CONTENT, {
    //     variables: {
    //         contentId:contentId,
    //         tagId:tagId
    //     }
    // });
    return (
        <div className="container w-full md:max-w-3xl mx-auto pt-20">
            11
        </div>
    );
}