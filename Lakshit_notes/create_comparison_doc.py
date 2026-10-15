from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.section import WD_SECTION
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.enum.style import WD_STYLE_TYPE

OUT = "Data_Analytics_Syllabus_and_Folder_Comparison.docx"

def shade(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = tcPr.find(qn('w:shd'))
    if shd is None:
        shd = OxmlElement('w:shd')
        tcPr.append(shd)
    shd.set(qn('w:fill'), fill)

def borders(table, color='D9D9D9', sz='6'):
    tbl = table._tbl
    tblPr = tbl.tblPr
    b = tblPr.first_child_found_in('w:tblBorders')
    if b is None:
        b = OxmlElement('w:tblBorders')
        tblPr.append(b)
    for edge in ('top','left','bottom','right','insideH','insideV'):
        tag = 'w:' + edge
        el = b.find(qn(tag))
        if el is None:
            el = OxmlElement(tag)
            b.append(el)
        el.set(qn('w:val'), 'single')
        el.set(qn('w:sz'), sz)
        el.set(qn('w:space'), '0')
        el.set(qn('w:color'), color)

def set_cell_text(cell, text, bold=False, color='000000', size=9.5):
    cell.text = ''
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.05
    r = p.add_run(text)
    r.bold = bold
    r.font.size = Pt(size)
    r.font.color.rgb = RGBColor.from_string(color)
    cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER

def add_table(doc, headers, rows, widths=None):
    table = doc.add_table(rows=1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = True
    borders(table)
    for i, h in enumerate(headers):
        set_cell_text(table.rows[0].cells[i], h, bold=True, color='FFFFFF', size=9)
        shade(table.rows[0].cells[i], '1F4E78')
    # Repeat the header on continuation pages and keep each body row together.
    trPr = table.rows[0]._tr.get_or_add_trPr()
    tbl_header = OxmlElement('w:tblHeader')
    tbl_header.set(qn('w:val'), 'true')
    trPr.append(tbl_header)
    for ridx, row in enumerate(rows):
        cells = table.add_row().cells
        row_pr = table.rows[-1]._tr.get_or_add_trPr()
        cant_split = OxmlElement('w:cantSplit')
        row_pr.append(cant_split)
        for i, value in enumerate(row):
            set_cell_text(cells[i], str(value), size=8.8)
            if ridx % 2 == 1:
                shade(cells[i], 'F3F6F9')
    if widths:
        for row in table.rows:
            for idx, w in enumerate(widths):
                row.cells[idx].width = Inches(w)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    return table

def add_bullet(doc, text, level=0):
    p = doc.add_paragraph(style='List Bullet' if level == 0 else 'List Bullet 2')
    p.paragraph_format.space_after = Pt(2)
    p.add_run(text)
    return p

doc = Document()
sec = doc.sections[0]
sec.top_margin = Inches(0.65)
sec.bottom_margin = Inches(0.65)
sec.left_margin = Inches(0.7)
sec.right_margin = Inches(0.7)

styles = doc.styles
styles['Normal'].font.name = 'Aptos'
styles['Normal'].font.size = Pt(10.5)
styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), 'Aptos')
for name, size, color in [('Title', 22, '000000'), ('Heading 1', 15, '000000'), ('Heading 2', 12, '000000')]:
    styles[name].font.name = 'Aptos Display' if name == 'Title' else 'Aptos'
    styles[name].font.size = Pt(size)
    styles[name].font.bold = True
    styles[name].font.color.rgb = RGBColor.from_string(color)

title = doc.add_paragraph(style='Title')
title.alignment = WD_ALIGN_PARAGRAPH.LEFT
title.add_run('Data Analytics Syllabus and Folder Comparison')
sub = doc.add_paragraph()
sub.paragraph_format.space_after = Pt(12)
r = sub.add_run('Coverage review of the syllabus PDF and Day1 to Day10 learning folders')
r.italic = True
r.font.size = Pt(11)
r.font.color.rgb = RGBColor.from_string('4F4F4F')

doc.add_heading('Purpose and conclusion', level=1)
p = doc.add_paragraph()
p.add_run('Purpose. ').bold = True
p.add_run('This document compares the course syllabus in 03_Data Analytics.pdf with the contents of the Day1 through Day10 folders. It identifies direct matches, partial matches, and syllabus topics that do not have a clear corresponding folder.')
p = doc.add_paragraph()
p.add_run('Conclusion. ').bold = True
p.add_run('The folders cover the early statistics, probability, correlation, data preparation, and exploratory analysis parts of the syllabus. The largest uncovered area is the later modelling and decision-analytics portion: predictive and prescriptive modelling, regression, forecasting, simulation, optimization, validation, classifier evaluation, factor analysis, and Power BI.')
p = doc.add_paragraph()
p.add_run('Interpretation rule. ').bold = True
p.add_run('“Covered” means the topic is explicitly present in a file name, readme, notebook title, or clearly identifiable folder subject. “Partial” means the folder is related, but the exact syllabus topic is not clearly demonstrated. The syllabus is session-based, so Day-to-session alignment is approximate.')

doc.add_heading('Source inventory', level=1)
add_table(doc, ['Source', 'What was reviewed'], [
    ['Syllabus PDF', '03_Data Analytics.pdf, 4 pages, Sessions 1–25'],
    ['Folders', 'Day1, Day2, Day3, Day4, Day5, Day6, Day7, Day8, Day9, Day10'],
    ['Folder materials', 'Python files, notebooks, Markdown/readme files, minutes, and the Day10 sample dataset'],
], [1.5, 5.8])

doc.add_heading('Day by day comparison', level=1)
rows = [
    ['Day1', 'Python foundations: closures, nested functions, decorators, polymorphism, mixins, generators, coroutines, context managers, threads, scope, partial functions', 'Sessions 1–2', 'Partial', 'Python is a prerequisite. The syllabus also includes business analytics introduction and the complete analytics life cycle, which are not represented by these Python exercises.'],
    ['Day2', 'NumPy arrays/tensors, vectorized operations, broadcasting, linear algebra, Pandas Series and DataFrames', 'Sessions 1–2', 'Partial', 'NumPy and Pandas are explicitly named in the syllabus lab. Specific advanced NumPy topics and Sklearn documentation/setup are not clearly present.'],
    ['Day3', 'Statistics basics, central tendency, dispersion, probability/statistics exercises', 'Session 5; Sessions 6–9', 'Mostly covered', 'Central tendency and dispersion align with Session 5. Sample spaces, conditional/marginal probability, Bayes theorem, sampling and estimation are not clearly evidenced.'],
    ['Day4', 'Percentiles, percentile methods, recap, skewness', 'Session 5; Sessions 11–12', 'Covered', 'Percentiles and skewness are explicitly named in the syllabus. The folder may contain implementation details beyond the syllabus wording.'],
    ['Day5', 'Deterministic domains/grids, functional and noisy signal population', 'Sessions 3, 6–8', 'Partial', 'Related to data nature and probability/distribution work, but the syllabus does not specifically name these signal/data-generation methods.'],
    ['Day6', 'Continuous probability distributions and measures of central tendency', 'Sessions 5 and 8', 'Mostly covered', 'Central tendency and distributions align. The syllabus topics of sample spaces, Bayes theorem, and the Central Limit Theorem are not clearly present.'],
    ['Day7', 'Dispersion, variability, position, distribution shape, covariance and Pearson correlation', 'Sessions 5, 10, 11–12', 'Mostly covered', 'The named measures, covariance, Pearson correlation, and skewness align. Explicit outlier handling and hypothesis tests are not clearly present.'],
    ['Day8', 'Covariance/Pearson correlation; Spearman and Kendall rank correlations', 'Session 10', 'Partial', 'Covariance and Pearson correlation match. Spearman and Kendall are extra folder topics; syllabus does not name them. Outlier handling is not clearly shown.'],
    ['Day9', 'Pandas indexing, vectorization, missing/malformed data, grouping, reshaping, large-data I/O', 'Sessions 1, 3–4', 'Partial', 'These support data preparation and exploratory analysis. The specific syllabus topics of analysis vs reporting, modern tools, visualization, and business decision case studies are not clearly covered.'],
    ['Day10', 'EDA, profiling tools, profiling exercises, sample dataset exploration', 'Session 4', 'Partial', 'Exploring data aligns with Session 4. The syllabus specifically calls for Matplotlib, Seaborn, and business decision case studies, which are not clearly demonstrated in the folder.'],
]
add_table(doc, ['Folder', 'Main folder topics', 'Closest syllabus sessions', 'Assessment', 'Comparison'], rows, [0.55, 2.05, 1.1, 0.85, 2.75])

doc.add_heading('Syllabus topics left after Day1 to Day10', level=1)
p = doc.add_paragraph('The following topics from the syllabus have no clear corresponding material in the reviewed folders, or only a weak/indirect connection.')
left_rows = [
    ['Sessions 1–3', 'Business Analytics introduction and case studies; analytics life cycle; model planning/building; quality assurance; documentation; management approval; installation, acceptance and operation; analysis versus reporting; modern data analytics tools'],
    ['Sessions 6–9', 'Sample spaces and events; joint, conditional and marginal probability; Bayes theorem; Central Limit Theorem; sampling and estimation; statistical interfaces'],
    ['Session 10', 'Explicit outlier handling as a lab task'],
    ['Sessions 11–12', 'Hypothesis testing; Z-test; Chi-square test'],
    ['Sessions 13–16', 'Predictive modelling concepts and tools; supervised segmentation; informative attributes; model induction and prediction; trees as rules; probability estimation; prescriptive modelling and use cases'],
    ['Sessions 17–18', 'Regression analysis; forecasting techniques'],
    ['Sessions 19–20', 'Simulation and risk analysis; linear and nonlinear optimization'],
    ['Sessions 21–22', 'Overfitting and avoidance; generalization; holdout versus cross-validation; decision analytics; classifier evaluation; analytical framework; baseline; performance and investment implications'],
    ['Session 23', 'Evidence and probabilities; explicit evidence combination with Bayes rule; probabilistic reasoning'],
    ['Session 24', 'Factor analysis; directional data analytics; functional data analysis'],
    ['Session 25', 'Power BI architecture and interface; Power Query; charts and reports; interactive dashboards; sharing insights'],
]
add_table(doc, ['Syllabus sessions', 'Topics not clearly covered in the folders'], left_rows, [1.2, 6.0])

doc.add_heading('Coverage summary', level=1)
add_table(doc, ['Area', 'Folder evidence', 'Syllabus status'], [
    ['Python, NumPy and Pandas foundations', 'Strong in Days 1–2', 'Partly aligned; Python is mainly a prerequisite'],
    ['Descriptive statistics', 'Strong in Days 3–4 and 6–7', 'Well aligned with Session 5'],
    ['Probability and distributions', 'Present in Days 5–6', 'Partially aligned; several named probability topics remain'],
    ['Correlation and distribution shape', 'Strong in Days 7–8', 'Mostly aligned; outliers and some methods remain'],
    ['Data wrangling and EDA', 'Strong in Days 9–10', 'Partially aligned with data preparation and exploration'],
    ['Predictive, prescriptive and decision analytics', 'No clear Day1–Day10 coverage', 'Major syllabus gap'],
    ['Regression, forecasting, simulation and optimization', 'No clear Day1–Day10 coverage', 'Major syllabus gap'],
    ['Validation, classifiers, factor analysis and Power BI', 'No clear Day1–Day10 coverage', 'Major syllabus gap'],
], [1.8, 2.3, 3.1])

doc.add_heading('Approximate remaining proportion', level=1)
p = doc.add_paragraph()
p.add_run('A precise percentage cannot be calculated from the PDF alone because the syllabus gives session topics and the folders contain a mixture of exercises, notebooks, and supporting material. ').bold = False
p.add_run('Using topic-level comparison, roughly 40% to 50% of the syllabus remains without clear folder coverage. ').bold = True
p.add_run('The estimate is driven mainly by Sessions 13–25, which are largely absent from Day1–Day10. It should be treated as an informed planning estimate, not an official course-completion percentage.')

doc.add_heading('Recommended next folders or study blocks', level=1)
for item in [
    'Hypothesis testing, Z-test, and Chi-square test.',
    'Predictive and prescriptive modelling, including segmentation and decision trees.',
    'Regression and forecasting.',
    'Simulation, risk analysis, and optimization.',
    'Overfitting, cross-validation, classifier evaluation, and decision analytics.',
    'Bayesian reasoning and explicit evidence combination.',
    'Factor analysis, directional data, and functional data analysis.',
    'Power BI, Power Query, dashboards, and report sharing.',
]:
    add_bullet(doc, item)

doc.add_paragraph()
foot = doc.add_paragraph()
foot.paragraph_format.space_before = Pt(8)
foot.add_run('Prepared from the local syllabus PDF and Day1–Day10 folder contents. ').italic = True
foot.add_run('Review date: 15 October 2026.').italic = True

doc.save(OUT)
print(OUT)
