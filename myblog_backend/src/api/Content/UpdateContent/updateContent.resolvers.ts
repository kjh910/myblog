import { Resolvers } from "src/types/resolvers";
import { UpdateContentResponse,UpdateContentMutationArgs } from "src/types/graph";
import Tag from "../../../entities/Tag";
import Content from "../../../entities/Content";

const resolvers:Resolvers = {
    Mutation: {
        UpdateContent: async (_,args:UpdateContentMutationArgs, {req}): Promise<UpdateContentResponse> => {
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
                        await Content.update(
                            {
                                id:args.contentId
                            },
                            {
                                content:args.content,
                                tagId:args.tagId
                            }
                        );
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