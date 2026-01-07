from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, ListFlowable, ListItem
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib import colors

# Create the PDF document
doc = SimpleDocTemplate(
    "Attardo-Resume.pdf",
    pagesize=A4,
    rightMargin=0.7*inch,
    leftMargin=0.7*inch,
    topMargin=0.6*inch,
    bottomMargin=0.6*inch
)

# Define colors
primary_color = HexColor('#1a365d')  # Dark blue
accent_color = HexColor('#2563eb')   # Bright blue
text_color = HexColor('#1f2937')     # Dark gray

# Get base styles and customize
styles = getSampleStyleSheet()

# Custom styles
styles.add(ParagraphStyle(
    name='MainTitle',
    parent=styles['Title'],
    fontSize=24,
    textColor=primary_color,
    spaceAfter=6,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold'
))

styles.add(ParagraphStyle(
    name='ContactInfo',
    parent=styles['Normal'],
    fontSize=10,
    textColor=text_color,
    alignment=TA_CENTER,
    spaceAfter=12
))

styles.add(ParagraphStyle(
    name='SectionTitle',
    parent=styles['Heading1'],
    fontSize=14,
    textColor=primary_color,
    spaceBefore=16,
    spaceAfter=8,
    fontName='Helvetica-Bold',
    borderPadding=(0, 0, 3, 0),
))

styles.add(ParagraphStyle(
    name='SubSection',
    parent=styles['Heading2'],
    fontSize=12,
    textColor=primary_color,
    spaceBefore=10,
    spaceAfter=4,
    fontName='Helvetica-Bold'
))

styles.add(ParagraphStyle(
    name='JobTitle',
    parent=styles['Normal'],
    fontSize=11,
    textColor=text_color,
    fontName='Helvetica-Bold',
    spaceBefore=8,
    spaceAfter=2
))

styles.add(ParagraphStyle(
    name='Company',
    parent=styles['Normal'],
    fontSize=10,
    textColor=accent_color,
    fontName='Helvetica-Oblique',
    spaceAfter=4
))

styles.add(ParagraphStyle(
    name='CustomBody',
    parent=styles['Normal'],
    fontSize=10,
    textColor=text_color,
    alignment=TA_JUSTIFY,
    spaceAfter=6,
    leading=14
))

styles.add(ParagraphStyle(
    name='BulletText',
    parent=styles['Normal'],
    fontSize=10,
    textColor=text_color,
    leftIndent=15,
    spaceAfter=3,
    leading=13
))

styles.add(ParagraphStyle(
    name='TechStack',
    parent=styles['Normal'],
    fontSize=9,
    textColor=HexColor('#4b5563'),
    fontName='Helvetica-Oblique',
    spaceBefore=4,
    spaceAfter=8
))

styles.add(ParagraphStyle(
    name='Tagline',
    parent=styles['Normal'],
    fontSize=11,
    textColor=accent_color,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold',
    spaceAfter=12
))

styles.add(ParagraphStyle(
    name='Summary',
    parent=styles['Normal'],
    fontSize=10,
    textColor=text_color,
    alignment=TA_JUSTIFY,
    spaceAfter=8,
    leading=14
))

# Build the document content
story = []

# Header
story.append(Paragraph("Elia A. Attardo, Ph.D.", styles['MainTitle']))
story.append(Paragraph("eattardo@gmail.com | Stuttgart, Germany | www.eattardo.info", styles['ContactInfo']))

# Tagline
story.append(Paragraph("Scientific Computing Specialist | High-Performance Computing | GPU Development", styles['Tagline']))

# Horizontal line
story.append(HRFlowable(width="100%", thickness=1, color=primary_color, spaceAfter=12))

# Summary
summary_text = """Computational physicist with 15+ years of experience in high-performance scientific computing and algorithm development.
Expert in GPU-accelerated computing (CUDA), parallel algorithms, and numerical methods for solving complex partial differential equations.
Proven track record of achieving 10-20x performance improvements through algorithmic optimization and hardware acceleration."""
story.append(Paragraph(summary_text, styles['Summary']))

summary_text2 = """Core expertise in computational electromagnetics with successful applications across biomedical imaging, industrial simulations,
and commercial software development. Strong mathematical foundation combined with practical engineering skills in C++ and CUDA programming."""
story.append(Paragraph(summary_text2, styles['Summary']))

# Areas of Expertise
story.append(Paragraph("Areas of Expertise", styles['SectionTitle']))
story.append(HRFlowable(width="100%", thickness=0.5, color=accent_color, spaceAfter=8))

expertise_items = [
    "<b>High-Performance Computing:</b> GPU acceleration (CUDA), multi-GPU systems, parallel algorithms, performance optimization",
    "<b>Scientific Computing:</b> Finite Element Methods (FEM), computational electromagnetics, inverse problems, numerical linear algebra",
    "<b>Algorithm Development:</b> Sparse and dense matrix solvers, preconditioners, domain decomposition methods, iterative solvers",
    "<b>Software Engineering:</b> C++, CUDA C/C++, Python, MATLAB, Wolfram Mathematica, software architecture",
    "<b>Mathematical Modeling:</b> PDEs, Integral Equations, optimization methods, medical imaging algorithms"
]

for item in expertise_items:
    story.append(Paragraph(f"• {item}", styles['BulletText']))

# Professional Experience
story.append(Paragraph("Professional Experience", styles['SectionTitle']))
story.append(HRFlowable(width="100%", thickness=0.5, color=accent_color, spaceAfter=8))

# Siemens
story.append(Paragraph("Software Engineer-Advanced", styles['JobTitle']))
story.append(Paragraph("Siemens Digital Industries Software, Germany | January 2026 – Present", styles['Company']))
story.append(Paragraph(
    "Developing high-performance electromagnetic simulation algorithms for Simcenter Feko within the Siemens Xcelerator ecosystem. "
    "Combining deep expertise in computational electromagnetics with modern AI-augmented development practices to accelerate innovation in solver technology.",
    styles['CustomBody']
))

siemens_items = [
    "GPU-accelerated electromagnetic solvers and HPC optimization",
    "Daily integration of generative AI and LLM-assisted coding for rapid prototyping, code generation, and technical documentation",
    "Numerical methods development (MoM, FEM, FDTD, hybrid approaches)",
    "Performance engineering and C++ modernization",
    "Investigating AI/ML applications in computational electromagnetics workflows"
]
for item in siemens_items:
    story.append(Paragraph(f"• {item}", styles['BulletText']))
story.append(Paragraph("<b>Technologies:</b> CUDA, C++, Intel MKL, OpenMP, MPI, NVIDIA Nsight, LLM-assisted development tools", styles['TechStack']))

# Altair
story.append(Paragraph("Senior Developer - Electromagnetic Solutions", styles['JobTitle']))
story.append(Paragraph("Altair Engineering GmbH, Germany | July 2014 – December 2025", styles['Company']))
story.append(Paragraph(
    "Developing high-performance algorithms for Altair Feko, a comprehensive computational electromagnetic software used globally "
    "for antenna design, electromagnetic compatibility, and radar cross-section analysis.",
    styles['CustomBody']
))

altair_items = [
    "Implemented GPU-accelerated ray tracing for electromagnetic optics, achieving <b>20x performance improvement</b> compared to single-core CPU",
    "Developed efficient preconditioners for sparse matrix equation systems, achieving <b>15x acceleration</b> compared to sequential code using Intel MKL",
    "Designed and implemented Discontinuous Galerkin Method for Integral Equations handling non-conformal meshes",
    "Optimized time-domain solver achieving <b>10x speedup</b> relative to sequential implementation",
    "Developed novel algorithms for metamaterial modeling within the FEM solver framework",
    "Led C++ development initiatives and code modernization efforts"
]
for item in altair_items:
    story.append(Paragraph(f"• {item}", styles['BulletText']))
story.append(Paragraph("<b>Technologies:</b> CUDA, C++, Intel MKL, OpenMP, MPI, GPU profiling tools (NVIDIA Nsight)", styles['TechStack']))

# Polytechnic Postdoc
story.append(Paragraph("Postdoctoral Research Fellow", styles['JobTitle']))
story.append(Paragraph("Polytechnic University of Turin, Italy | July 2013 – June 2014", styles['Company']))
postdoc_items = [
    "Developed GPU-accelerated algorithms for computational electromagnetic applications in biomedical and industrial contexts",
    "Implemented fast and reliable solvers integrated into the MICENEA project",
    "Focus on high-performance computing solutions for real-time medical imaging applications"
]
for item in postdoc_items:
    story.append(Paragraph(f"• {item}", styles['BulletText']))

# ISMB
story.append(Paragraph("Researcher", styles['JobTitle']))
story.append(Paragraph("Istituto Superiore Mario Boella, Turin, Italy | January 2011 – June 2014", styles['Company']))
ismb_items = [
    "Designed and simulated RF devices and antennas in complex media",
    "Lead computational researcher on RADIODRY industrial project",
    "Developed numerical models for electromagnetic wave propagation in heterogeneous materials"
]
for item in ismb_items:
    story.append(Paragraph(f"• {item}", styles['BulletText']))

# NE Scientific
story.append(Paragraph("Early Company Member - Computational Scientist", styles['JobTitle']))
story.append(Paragraph("NE Scientific LLC, Boston, MA, USA | January 2011 – December 2013", styles['Company']))
nes_items = [
    "Developed GPU-accelerated sparse linear solver for medical imaging applications",
    "Achieved <b>8x speedup</b> compared to Intel PARDISO MKL on sequential core",
    "Implemented parallel algorithms for real-time image reconstruction"
]
for item in nes_items:
    story.append(Paragraph(f"• {item}", styles['BulletText']))

# Dartmouth
story.append(Paragraph("Research Assistant - High-Performance Computing", styles['JobTitle']))
story.append(Paragraph("Thayer School of Engineering, Dartmouth College, Hanover, NH, USA | January 2011 – August 2011", styles['Company']))
dartmouth_items = [
    "Developed HPC algorithms for multi-modal image guidance system (NIH Grant: 1RC1EB011000-01)",
    "Achieved <b>20x acceleration</b> of imaging algorithms using multi-GPU systems",
    "Implemented parallel computing solutions for real-time prostate biopsy guidance"
]
for item in dartmouth_items:
    story.append(Paragraph(f"• {item}", styles['BulletText']))

# Education
story.append(Paragraph("Education", styles['SectionTitle']))
story.append(HRFlowable(width="100%", thickness=0.5, color=accent_color, spaceAfter=8))

story.append(Paragraph("Ph.D. Electronics and Communications Engineering", styles['JobTitle']))
story.append(Paragraph("Polytechnic University of Turin, Italy | 2008 – 2011", styles['Company']))
story.append(Paragraph("<i>Dissertation: Computational Methods for Microwave Imaging - Biomedical Applications</i><br/>Focus: GPU-accelerated algorithms, inverse scattering problems, high-performance computing", styles['CustomBody']))

story.append(Paragraph("M.Sc. (Laurea Specialistica), Biomedical Engineering", styles['JobTitle']))
story.append(Paragraph("Polytechnic University of Turin, Italy | 2005 – 2007", styles['Company']))
story.append(Paragraph("<i>Thesis: Microwave Tomography for Breast Cancer Detection</i><br/>Focus: Computational modeling, signal processing, medical imaging", styles['CustomBody']))

story.append(Paragraph("B.Sc. (Laurea Triennale), Software Engineering", styles['JobTitle']))
story.append(Paragraph("University of Palermo, Italy | 2001 – 2004", styles['Company']))
story.append(Paragraph("<i>Thesis: Noise Reduction in Magnetic Resonance Imaging</i><br/>Focus: Algorithm development, image processing", styles['CustomBody']))

# Technical Skills
story.append(Paragraph("Technical Skills", styles['SectionTitle']))
story.append(HRFlowable(width="100%", thickness=0.5, color=accent_color, spaceAfter=8))

skills_data = [
    ["<b>High-Performance Computing</b>", "CUDA, OpenCL, MPI, OpenMP, multi-threading, distributed computing, NVIDIA Nsight, Intel VTune"],
    ["<b>Scientific Computing</b>", "FEM, BEM, FDTD, spectral methods, sparse/dense matrix solvers, iterative methods, preconditioning"],
    ["<b>Libraries</b>", "Intel MKL, cuBLAS, cuSPARSE, cuSolver, cuDSS, LAPACK, PETSc"],
    ["<b>Languages & Tools</b>", "C++, CUDA C/C++, Python, Fortran, Git, CMake, CI/CD, HPC clusters"]
]

for row in skills_data:
    story.append(Paragraph(f"• {row[0]}: {row[1]}", styles['BulletText']))

# Selected Publications
story.append(Paragraph("Selected Publications", styles['SectionTitle']))
story.append(HRFlowable(width="100%", thickness=0.5, color=accent_color, spaceAfter=8))

publications = [
    "<b>Attardo E.A.</b>, Delgado C., Van Tonder J., Zhabitskiy I., Garcia E., Jakobus U. (2025) – A High-Performance Multi-Core Hierarchical Preconditioner for Multiscale Electromagnetic Problems with the MLFMM, IEEE URSI Kleinheubacher Tagung 2025",
    "<b>Attardo E.A.</b>, Borsic A. (2012) – GPU Acceleration of Algebraic Multigrid for Low-Frequency Finite Element Methods – IEEE APS/URSI",
    "Borsic A., <b>Attardo E.A.</b>, Halter R. (2012) – Multi-GPU Jacobian Accelerated Computing for Soft Field Tomography, Physiological Measurements",
    "<b>Attardo E.A.</b>, Vecchi G., Crocco L. (2014) – Contrast Source Extended Born Inversion in Noncanonical Scenarios via FEM Modeling, IEEE TAP"
]

for pub in publications:
    story.append(Paragraph(f"• {pub}", styles['BulletText']))

story.append(Paragraph("<i>Full publication list: 30+ papers available at www.eattardo.info</i>", styles['TechStack']))

# Certifications
story.append(Paragraph("Certifications", styles['SectionTitle']))
story.append(HRFlowable(width="100%", thickness=0.5, color=accent_color, spaceAfter=8))

story.append(Paragraph("<b>Deep Learning / AI:</b> NVIDIA Getting Started with Deep Learning, Neural Networks and Deep Learning (Coursera), Supervised Machine Learning, Advanced Learning Algorithms", styles['BulletText']))
story.append(Paragraph("<b>Blockchain:</b> Certified Blockchain Expert, Certified Solidity Developer, Smart Contracts (Coursera)", styles['BulletText']))

# Professional Activities & Languages
story.append(Paragraph("Professional Activities", styles['SectionTitle']))
story.append(HRFlowable(width="100%", thickness=0.5, color=accent_color, spaceAfter=8))

activities = [
    "Reviewer for IEEE Transactions on Antennas and Propagation",
    "Member of Applied Computational Electromagnetics Society (ACES)",
    "Regular presenter at IEEE APS/URSI and ACES conferences"
]
for item in activities:
    story.append(Paragraph(f"• {item}", styles['BulletText']))

story.append(Spacer(1, 8))
story.append(Paragraph("<b>Languages:</b> English (Fluent), Italian (Native), German (Intermediate)", styles['CustomBody']))

# Build PDF
doc.build(story)
print("PDF generated successfully: /home/claude/Elia_Attardo_CV.pdf")
