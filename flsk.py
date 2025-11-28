from flask import Flask

app = Flask(__name__)



RESUME_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Digital Resume - AYUSH RAJ</title>

    <style>
        /* General Reset & Typography */
        body {
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #f4f4f9; /* Light, professional background */
            color: #333;
            line-height: 1.6;
        }

        /* Main Layout Container */
        .container {
            max-width: 900px;
            margin: 40px auto;
            padding: 30px;
            background: #ffffff;
            border-radius: 8px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }

        /* Header */
        header {
            text-align: center;
            padding-bottom: 15px;
            border-bottom: 3px solid #E85D04; /* Used a warm, engaging color */
            margin-bottom: 25px;
        }

        .name {
            font-size: 2.5rem;
            margin: 0;
            font-weight: 700;
            color: #1a1a1a;
        }

        .tagline {
            font-size: 1.2rem;
            margin: 5px 0 0 0;
            color: #E85D04;
            font-weight: 500;
        }
        
        .contact-info {
            font-size: 0.95rem;
            color: #777;
            margin-top: 10px;
        }

        .contact-info a {
            color: #E85D04;
            text-decoration: none;
            margin: 0 8px;
        }

        .contact-info a:hover {
            text-decoration: underline;
        }

        /* Section Styling */
        section {
            margin-bottom: 30px;
        }

        section h2 {
            font-size: 1.6rem;
            color: #333;
            margin-bottom: 15px;
            border-bottom: 2px solid #eee;
            padding-bottom: 5px;
            font-weight: 600;
        }

        /* List Styling (Creative Interests, Experience) */
        .interests ul,
        .experience-item ul {
            list-style-type: square;
            padding-left: 25px;
            margin-top: 5px;
        }
        
        /* Item Styling (Education, Experience) */
        .edu-item,
        .experience-item {
            margin-bottom: 15px;
            padding: 10px;
            border-left: 4px solid #E85D04;
            background-color: #fcfcfc;
        }

        .item-title {
            font-size: 1.15rem;
            margin: 0 0 3px 0;
            color: #222;
            font-weight: 600;
        }

        .item-meta {
            font-size: 0.9rem;
            color: #555;
            margin: 0;
        }
        
        .skill-group {
            margin-bottom: 10px;
        }
        
        .skill-group p {
            margin: 3px 0;
        }

        /* Footer */
        footer {
            text-align: center;
            margin-top: 30px;
            padding-top: 15px;
            border-top: 1px solid #ddd;
            font-size: 0.85rem;
            color: #999;
        }
    </style>

</head>
<body>

    <div class="container">

        <header>
            <h1 class="name">AYUSH RAJ</h1>
            <p class="tagline">SOCIAL MEDIA ENTHUSIAST</p>
            <p class="contact-info">
                <a href="tel:9534193446">9534193446</a> | 
                <a href="mailto:ayushakabewakoof@gmail.com">ayushakabewakoof@gmail.com</a> |
                <a href="https://www.instagram.com/_ay._.ush__" target="_blank">Instagram: @_ay._.ush__</a>
            </p>
        </header>

        <section class="about">
            <h2>About Me</h2>
            <p>
                Highly creative and analytical B.Tech undergraduate with a technical foundation in CSE and AI-ML that fuels a data-driven approach to marketing. I possess a genuine passion for digital storytelling and content optimization, demonstrated through my skills in Filmmaking, Photography, and Graphic Design[cite: 2]. Eager to transition my problem-solving and optimization expertise into driving engaging social media campaigns, measuring their effectiveness, and contributing to brand growth as a Marketing Trainee[cite: 3].
            </p>
        </section>

        <section class="experience">
            <h2>Experience & Achievement</h2>
            <div class="experience-item">
                <h3 class="item-title">Social Media Manager</h3>
                <p class="item-meta">V studios Vgu | 2024 - Present [cite: 5]</p>
                <ul>
                    <li>Covered the Khelo Creators League Rajasthan, shooting BTS and stills, representing Vstudios VGU[cite: 6].</li>
                    <li>Creatively assisting Vstudios and some small businesses and artists around[cite: 7].</li>
                    <li>Covered the SABARMATI REPORT movie promotional event featuring Vikrant Massey[cite: 8].</li>
                    <li>Made a complete mobile-shot short film **ROOM 101** on YouTube with 17k views till now[cite: 8].</li>
                    <li>Posts regular Filmmaking and Photography content on social media[cite: 9].</li>
                    <li>Performed in the literature fest of Indian Maritime University Kolkata for storytelling for a crowd of 500 persons[cite: 9].</li>
                </ul>
            </div>
        </section>

        <section class="skills">
            <h2>Skills & Creative Interests</h2>
            
            <div class="skill-group">
                <h3 class="item-title" style="margin-bottom: 5px;">Creative & Soft Skills</h3>
                <p class="item-meta">Content Creation, Photography & Videography, Graphic Design (Canva basics), Digital Storytelling, Verbal & Written Communication, Teamwork & Collaboration.</p>
            </div>
            
            <div class="skill-group">
                <h3 class="item-title" style="margin-bottom: 5px;">Digital & Analytical Skills</h3>
                <p class="item-meta">Social Media Platforms (Instagram, YouTube), Basic Google Analytics, SEO/SEM Concepts[cite: 12].</p>
            </div>
            
            <div class="skill-group interests">
                 <h3 class="item-title" style="margin-bottom: 5px;">Key Creative Interests</h3>
                 <ul>
                    <li>**Photography & Graphic Design:** Experienced in visual composition and creating engaging digital assets[cite: 10].</li>
                    <li>**Filmmaking & Screenwriting:** Skilled in creating structured narratives and producing short-form video content[cite: 11].</li>
                 </ul>
            </div>
        </section>

        <section class="education">
            <h2>Education</h2>
            <div class="edu-item">
                <h3 class="item-title">B-tech in Computer Science with specialization in Ai-MI</h3>
                <p class="item-meta">Vivekananda Global University, Jaipur | 2024 - Present </p>
                <p class="item-meta">Current GPA: 8.5 </p>
            </div>
        </section>

        <footer>
            <p>Generated with Python Flask | Content based on Ayush Raj's Resume</p>
        </footer>

    </div>

</body>
</html>
"""


@app.route("/")
def home():
    """
    Returns the complete HTML structure for the professional resume.
    """
    return RESUME_HTML


if __name__ == "__main__":
    # Use host='127.0.0.1' for local access, debug=True for development
    app.run(host='127.0.0.1', port=5000, debug=True)