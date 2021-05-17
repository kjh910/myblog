import { Resolvers } from "src/types/resolvers";
import { CreateTagResponse,CreateTagMutationArgs } from "src/types/graph";
import Tag from "../../../entities/Tag";

const resolvers:Resolvers = {
    Mutation: {
        CreateTag: async (_,args:CreateTagMutationArgs, {req}): Promise<CreateTagResponse> => {
            try{
                Tag.create(
                    {
                        tagName:args.tagName
                    }
                ).save()

                return {
                    ok:true,
                    error:null
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