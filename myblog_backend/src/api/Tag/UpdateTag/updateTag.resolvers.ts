import { Resolvers } from "src/types/resolvers";
import { UpdateTagResponse,UpdateTagMutationArgs } from "src/types/graph";
import Tag from "../../../entities/Tag";

const resolvers:Resolvers = {
    Mutation: {
        UpdateTag: async (_,args:UpdateTagMutationArgs, {req}): Promise<UpdateTagResponse> => {
            try{
                const tag = await Tag.findOne(
                    {
                        id:args.tagId,
                    },
                    {
                        relations:['contents']
                    }
                );

                if(tag){
                    await Tag.update(
                        {
                            id:args.tagId
                        },
                        {
                            tagName:args.tagName
                        }
                    );
                    return {
                        ok:true,
                        error:null
                    }
                } else {
                    return {
                        ok:false,
                        error:'Not Found Tag'
                    }
                }
            } catch(e){
                return {
                    ok:false,
                    error:e.message
                }
            }
        }
    }
    
}

export default resolvers;