import { Resolvers } from "src/types/resolvers";
import { DeleteTagResponse,DeleteTagMutationArgs } from "src/types/graph";
import Tag from "../../../entities/Tag";
import Content from "../../../entities/Content";

const resolvers:Resolvers = {
    Mutation: {
        DeleteTag: async (_,args:DeleteTagMutationArgs, {req}): Promise<DeleteTagResponse> => {
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
                    const content = await Content.find(
                        {
                            relations:['tag'],
                            where:{
                                tagId: args.tagId
                            }
                        }
                    );
                    if(content){
                        await Content.softRemove(content);
                    }
                    await Tag.softRemove(tag);
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