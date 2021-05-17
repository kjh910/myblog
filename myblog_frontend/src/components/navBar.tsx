import { gql, useQuery } from "@apollo/client";
import React, { Fragment } from "react";
import { GetAllTag } from "../__generated__/GetAllTag";

const GET_ALL_TAG_NAME = gql`
    query GetAllTag{
        GetAllTag{
            ok
            error
            tags{
                tagName
                id
            }
        }
    }
`;

export const NavBar = () => {
    const {data} = useQuery<GetAllTag>(GET_ALL_TAG_NAME);
    return (
        <div className="container w-full md:max-w-3xl mx-auto pt-20 pl-20">
            <div className="text-gray-900 text-base no-underline hover:no-underline font-extrabold text-xl">CategoryList</div> <br />
        
            <div className=" mb-3 text-xs text-gray-700 ">
                
                {data?.GetAllTag.tags?.map((tag) => (
                    <div className="flex mb-1">
                        {tag?.tagName}
                    </div>
                ))} 
            </div>
        </div>
    );
}