import Content from "../../../entities/Content";
import { Resolvers } from "src/types/resolvers";
import { GetContentResponse, GetContentQueryArgs } from "src/types/graph";

const resolvers: Resolvers = {
    Query: {
        GetContent: async (_,args:GetContentQueryArgs,{req}): Promise<GetContentResponse> => {
            try{
                const content = await Content.findOne(
                    {
                        id:args.contentId
                    },
                    {
                        relations: ['tag'],
                        where:{
                            tagId: args.tagId
                        }
                    }
                );
                if(content){
                    return {
                        ok:true,
                        error:null,
                        content
                    };
                } else {
                    return {
                        ok:false,
                        error:'Not Found Content',
                        content:null
                    };
                }
            } catch(e){
                return {
                    ok:false,
                    error:e.message,
                    content:null
                }   
            }
        }
    }
};

export default resolvers;