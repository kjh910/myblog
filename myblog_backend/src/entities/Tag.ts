import {
  BaseEntity,
  Column,
  CreateDateColumn,
  DeleteDateColumn,
  Entity,
  OneToMany,
  PrimaryGeneratedColumn,
  UpdateDateColumn
} from "typeorm";
import Content from "./Content";

@Entity()
class Tag extends BaseEntity {
    @PrimaryGeneratedColumn() id: number;

    @Column({ type: "text"})
    tagName: string;

    @OneToMany(type => Content, content => content.tag)
    contents: Content[];

    @CreateDateColumn() 
    createdAt: string;

    @UpdateDateColumn() 
    updatedAt: string;

    @DeleteDateColumn()
    deletedAt?: Date
}

export default Tag;