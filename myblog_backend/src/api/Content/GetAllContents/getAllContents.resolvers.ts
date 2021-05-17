import Content from "../../../entities/Content";
import { Resolvers } from "src/types/resolvers";
import { GetAllContentsResponse,GetAllContentsQueryArgs } from "src/types/graph";
const resolvers: Resolvers = {
    Query: {
        GetAllContents: async (_,args:GetAllContentsQueryArgs,{req}): Promise<GetAllContentsResponse> => {
            try{
                if(args.tagId && args.tagId != 0){
                    console.log(args.tagId)
                    const content:Content[] = await Content.find({
                        relations:['tag'],
                        where:{
                            tagId: args.tagId
                        }
                    });
                    if(content.length > 0){
                        return {
                            ok:true,
                            error:null,
                            contents:content
                        };
                    } else {
                        return {
                            ok:false,
                            error:'Not Found Content',
                            contents:null
                        };
                    }
                } else {
                    const allContents:Content[] = await Content.find(
                        {
                            relations:['tag']
                        }
                    );

                    if(allContents.length > 0){
                        return {
                            ok:true,
                            error:null,
                            contents:allContents
                        };
                    } else {
                        return {
                            ok:false,
                            error:'Not Found Content',
                            contents:null
                        };
                    }

                }
            } catch(e){
                return {
                    ok:false,
                    error:e.message,
                    contents:null
                }   
            }
        }
    }
};

export default resolvers;