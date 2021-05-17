import Tag from "../../../entities/Tag";
import { Resolvers } from "src/types/resolvers";
import { GetTagQueryArgs, GetTagResponse } from "src/types/graph";

const resolvers: Resolvers = {
    Query: {
        GetTag: async (_,args:GetTagQueryArgs ,{req}): Promise<GetTagResponse> => {
            try{
                const tag = await Tag.findOne(
                    {
                        id:args.tagId,
                    },
                    {
                        relations:['contents'],
                        where:{
                            isDeleted: false
                        }
                    }
                );
                if(tag){
                    return {
                        ok:true,
                        error:null,
                        tag
                    };
                } else {
                    return {
                        ok:false,
                        error:'Not Found Tag',
                        tag:null
                    };
                }
            } catch(e){
                return {
                    ok:true,
                    error:e.message,
                    tag:null
                }   
            }
        }
    }
};

export default resolvers;