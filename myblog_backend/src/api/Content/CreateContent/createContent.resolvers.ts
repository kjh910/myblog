import { Resolvers } from "src/types/resolvers";
import { CreateContentResponse,CreateContentMutationArgs } from "src/types/graph";
import Content from "../../../entities/Content";
import Tag from "../../../entities/Tag";

const resolvers:Resolvers = {
    Mutation: {
        CreateContent: async (_,args:CreateContentMutationArgs, {req}): Promise<CreateContentResponse> => {
            try{
                const tag = await Tag.findOne(
                    {
                        id:args.tagId
                    },
                    {
                        relations:['contents']
                    }
                )
                if(tag){
                    Content.create(
                        {
                            tagId:args.tagId,
                            content:args.content
                        }
                    ).save();
                    return {
                        ok:true,
                        error: null
                    }
                } else {
                    return {
                        ok:false,
                        error: 'not found tag'
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