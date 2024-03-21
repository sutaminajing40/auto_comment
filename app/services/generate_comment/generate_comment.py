from common.llm import openai_chat
from db import db
from langchain_core.output_parsers import StrOutputParser
from models.models import comment
from services.generate_comment.prompt import generate_comment_prompt_template

COMMENT_LIMIT = 5
LLM = openai_chat


def generate_comment(content: str):
    task_id = content.split(' ', 1)[0]
    task_comments = get_comments_by_task_id(task_id, COMMENT_LIMIT)
    output_parser = StrOutputParser()

    generate_comment_chain = (
        generate_comment_prompt_template
        | LLM
        | output_parser
    )

    generated_comment = generate_comment_chain.invoke(
        {"example1": task_comments[0].content, "task_id": task_id})
    return generated_comment


def get_comments_by_task_id(task_id: str, k: int) -> list[comment]:
    comments = comment.query.filter_by(task_id=task_id).limit(k).all()
    db.session.commit()
    return comments
