import Tag from "../../../entities/Tag";
import { Resolvers } from "src/types/resolvers";
import { GetAllTagResponse } from "src/types/graph";
// import { getRepository } from "typeorm";

const resolvers: Resolvers = {
    Query: {
        GetAllTag: async (_,__,{req}): Promise<GetAllTagResponse> => {
            try{
                const tag: Tag[] = await Tag.find(
                    {
                        relations:['contents']
                    }
                );
                if(tag){
                    return {
                        ok:true,
                        error:null,
                        tags:tag
                    };
                } else {
                    return {
                        ok:false,
                        error:'Not Found Tag',
                        tags:null
                    };
                }
            } catch(e){
                return {
                    ok:false,
                    error:e.message,
                    tags:null
                }   
            }
        }
    }
};

export default resolvers;