# -*- coding: utf-8 -*-
"""all-MiniLM-L6-v2 WebUI：句子嵌入与相似度演示（前端展示，不加载实际模型）"""
import gradio as gr

def on_load_model(model_path):
    if not model_path or not model_path.strip():
        return "未加载"
    return "就绪"

def on_similarity(sent1, sent2, model_status):
    if model_status != "就绪":
        return "请先加载模型。"
    if not sent1 or not sent2:
        return "请填写两句待比较的文本。"
    return "[演示] 两句文本的模拟相似度：0.85。实际使用需加载 all-MiniLM-L6-v2 并调用 encode 与相似度计算。"

with gr.Blocks(title="all-MiniLM-L6-v2 测试") as demo:
    gr.Markdown("# all-MiniLM-L6-v2 句子相似度 · WebUI 演示")
    gr.Markdown("本界面以交互方式展示 all-MiniLM-L6-v2 的典型使用流程，包括模型加载与句子相似度结果展示。")
    with gr.Row():
        with gr.Column(scale=1):
            model_path = gr.Textbox(label="模型路径", placeholder="例如：sentence-transformers/all-MiniLM-L6-v2", value="")
            load_btn = gr.Button("加载模型（演示）", variant="primary")
        with gr.Column(scale=2):
            load_status = gr.Textbox(label="模型状态", interactive=False, value="尚未加载")
    load_btn.click(fn=on_load_model, inputs=[model_path], outputs=[load_status])
    gr.Markdown("---")
    gr.Markdown("### 句子相似度")
    gr.Markdown("在下方输入两个句子，模型将计算其语义相似度（演示模式返回模拟值）。")
    with gr.Row():
        sent1 = gr.Textbox(label="句子 A", placeholder="例如：This is an example sentence", lines=2)
        sent2 = gr.Textbox(label="句子 B", placeholder="例如：Each sentence is converted", lines=2)
    sim_btn = gr.Button("计算相似度（演示）", variant="secondary")
    result = gr.Textbox(label="相似度结果", interactive=False, lines=2)
    sim_btn.click(fn=on_similarity, inputs=[sent1, sent2, load_status], outputs=[result])
    gr.Markdown("---")
    gr.Markdown("*说明：当前为轻量级演示界面，未实际下载与加载 all-MiniLM-L6-v2 模型参数。*")

if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=17960)
