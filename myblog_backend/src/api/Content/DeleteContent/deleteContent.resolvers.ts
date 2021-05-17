import { Resolvers } from "src/types/resolvers";
import { DeleteContentResponse,DeleteContentMutationArgs } from "src/types/graph";
import Tag from "../../../entities/Tag";
import Content from "../../../entities/Content";

const resolvers:Resolvers = {
    Mutation: {
        DeleteContent: async (_,args:DeleteContentMutationArgs, {req}): Promise<DeleteContentResponse> => {
            try{
                const tag = await Tag.findOne(
                    {
                        id:args.tagId
                    },
                    {
                        relations:['contents']
                    }
                );

                if(tag){
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
                        await Content.softRemove(content);
                        return {
                            ok:true,
                            error:null
                        }
                    } else {
                        return {
                            ok:false,
                            error:'Not Found Content'
                        }
                    }
                } else{
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