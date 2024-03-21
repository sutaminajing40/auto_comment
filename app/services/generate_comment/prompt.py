from langchain_core.prompts import ChatPromptTemplate

generate_comment_prompt_template = ChatPromptTemplate.from_template(
    """
    あなたはプログラミング教室の授業コメントを生成するアシスタントです。
    以下の例文を元に、コメントを生成してください。
    以下の条件を満たすようにコメントを生成してください。

    ### 条件 ###
    - ポジティブなコメントを生成してください。
    - task_idに含まれる数字を頭につけて半角スペースの後にコメント内容を記入してください。

    ### 例文 ###
    例文1: {example1}

    ### 入力 ###
    task_id: {task_id}

    ### 出力 ###
    {task_id} ここにコメントを記入する。
    """
)
