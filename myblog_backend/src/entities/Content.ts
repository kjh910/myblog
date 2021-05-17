import {
  BaseEntity,
  Column,
  CreateDateColumn,
  DeleteDateColumn,
  Entity,
  ManyToOne,
  PrimaryGeneratedColumn,
  UpdateDateColumn
} from "typeorm";
import Tag from "./Tag";
  
@Entity()
class Content extends BaseEntity {
    @PrimaryGeneratedColumn() id: number;

    @Column({ type: "text"})
    content:string;

    @ManyToOne(type => Tag, tag => tag.contents,
      { orphanedRowAction: 'delete' }
    )
    tag:Tag;

    @Column()
    tagId: number;

    @CreateDateColumn() 
    createdAt: string;

    @UpdateDateColumn() 
    updatedAt: string;
    
    @DeleteDateColumn()
    deletedAt?: Date
}

export default Content;