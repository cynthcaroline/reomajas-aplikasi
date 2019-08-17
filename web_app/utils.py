from docxtpl import DocxTemplate


result_path = 'media/result/report.docx'

def gerate_report(data: dict):
    template = DocxTemplate("media/template/template.docx")
    context = data
    template.render(context)
    template.save(result_path)