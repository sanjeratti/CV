"""
Все данные резюме собраны в одном месте.
Чтобы отредактировать резюме — меняйте только этот файл,
index.html трогать больше не нужно.
"""

RESUME_DATA = {
    "name": "Sanzhar Abdykerimov",
    "title": "QA Automation engineer | Test Engineer",

    "about_heading": "QA Automation engineer | Python Web Developer Located In Our Lovely Earth",
    "about_text": (
        "Experienced QA Automation Engineer and Python Web Developer with a strong background in "
        "designing, developing, and maintaining automated test scripts and web applications. "
        "Proficient in Java, Python, and various testing frameworks, including Selenium WebDriver "
        "and Pytest. Skilled in building robust RESTful APIs using Django and FastAPI, managing "
        "databases with PostgreSQL, MySQL, MongoDB and SQLite, and implementing CI/CD pipelines "
        "with Docker, Jenkins and GitLab CI. Adept at collaborating in Agile Scrum environments, "
        "ensuring high-quality code through rigorous testing, and leveraging modern tools for "
        "monitoring and performance optimization. Proven track record of translating complex "
        "requirements into technical specifications and delivering scalable solutions. Seeking "
        "opportunities in European companies with relocation options."
    ),

    "contacts": {
        "email": "sanzhar.abdykerimov@gmail.com",
        "phone": "+ (49) 15203210138",
        "linkedin_url": "https://www.linkedin.com/in/sanzhar-abdykerimov/",
        "linkedin_label": "https://www.linkedin.com/in/sanzhar-abdykerimov/",
        "github_url": "https://github.com/Sanjeratti",
        "github_label": "Sanjeratti",
    },

    "expertise": [
        {
            "icon": "ti-widget",
            "title": "QA Automation",
            "subtitle": "Selenium WebDriver, TestNG, Pytest, REST Assured",
        },
        {
            "icon": "ti-paint-bucket",
            "title": "Web Development",
            "subtitle": "Django, FastAPI, DRF, PostgreSQL, MySQL, MongoDB, SQLite",
        },
        {
            "icon": "ti-stats-up",
            "title": "Financial Analysis",
            "subtitle": "Excel, Macros, Budget Planning, Data Analysis with Large Tables",
        },
    ],

    "experience": [
        {
            "period": "2017 - Present",
            "role": "QA Automation engineer | Python Web Developer | Lightcode DEVs LLC, Bishkek, Kyrgyzstan",
            "description": (
                "Responsibilities as a QA Automation Engineer:\n"
                "Automated Testing Execution: Conducting comprehensive Front-end, Back-end, Functional, "
                "API, Smoke, Regression, and End-to-end testings to ensure the robustness and "
                "functionality of software products.\n"
                "Programming Expertise: Applying strong knowledge of the JAVA programming language and "
                "Object-Oriented Programming (OOP) concepts to develop and maintain automation frameworks "
                "and scripts.\n"
                "Utilization of Automation Tools: Employing framework build tools like Maven and "
                "automation tools like Selenium WebDriver with Java, TestNG, JUnit, Cucumber, and REST "
                "Assured for testing Client-Server and Web-based Applications.\n"
                "BDD Implementation: Implementing Behavior Development (BDD) using the Cucumber feature, "
                "Scenarios, and Step Definitions, for writing test scripts, and test cases.\n"
                "Responsibilities as a Python Web Developer:\n"
                "Web Application Development: Leveraging Python frameworks such as Django, Django Rest "
                "Framework (DRF), and FastAPI for developing and maintaining OOP scalable and "
                "user-friendly web applications.\n"
                "Technological Proficiency: Skillfully engaging with technologies like Grafana, "
                "Zookeeper, Kafka, ClickHouse, Elasticsearch, and Kibana to optimize application "
                "performance and facilitate efficient data analysis.\n"
                "Overall responsibilities:\n"
                "Database Management: Effectively managing PostgreSQL, MySQL, MongoDB, and SQLite "
                "databases to ensure seamless integration and data management within web applications.\n"
                "Containerization with Docker: Utilizing Docker for containerization, simplifying "
                "application deployment and management procedures.\n"
                "Continuous Integration and Version Control: Executing Continuous Integration using "
                "Jenkins, integrating Git/GitHub for efficient version control, and managing the base "
                "code.\n"
                "Agile Scrum Involvement: Participating in Agile Scrum ceremonies such as Sprint "
                "Grooming, Sprint Planning, Sprint Retrospective, and Scrum meetings to ensure "
                "collaboration and efficiency within the development team."
            ),
        },
        {
            "period": "2018 - 2020",
            "role": "Lead program analyst engineer | OJSC Electric Power Plants, Bishkek, Kyrgyzstan",
            "description": (
                "Orchestrating Sprint Activities: Acted as a pivotal liaison between developers and "
                "finance professionals, ensuring seamless coordination and collaboration within sprint "
                "cycles.\n"
                "Translating Finance Team Requirements: Transformed intricate finance team requirements "
                "into comprehensive technical specifications for the 1C software, facilitating a smooth "
                "alignment between technical functionalities and financial needs.\n"
                "Overseeing Customization and Compliance: Led the oversight of customizing 1C software "
                "to meet specific finance team requisites, ensuring strict adherence to finance "
                "regulations and local legislation.\n"
                "Developing User Manuals and Guidelines: Spearheaded the development and maintenance of "
                "user manuals and guidelines, enhancing user experience and operational efficiency "
                "within the finance domain."
            ),
        },
        {
            "period": "2017 - 2018",
            "role": "QA engineer in test | lberKyrgyz Wealth Group ltd., Bishkek, Kyrgyzstan",
            "description": (
                "Software Testing and Reporting: Conduct comprehensive manual testing of software "
                "application to identify defects, document issues accurately, and report findings to "
                "the development team using established protocols and tools.\n"
                "User Training and Software Presentation: Assist in presenting software functionalities "
                "to users, providing training and support as needed, ensuring a smooth user experience, "
                "and addressing queries or concerns."
            ),
        },
        {
            "period": "2011 - 2016",
            "role": "Senior Financial analyst | OJSC Optima Bank, Bishkek, Kyrgyzstan",
            "description": (
                "Financial Analysis: Conduct comprehensive financial analysis to assess the bank's "
                "performance, including analyzing financial statements, evaluating financial risks, and "
                "identifying opportunities for improvement.\n"
                "Budgeting and Forecasting: Lead the budgeting process by developing financial "
                "forecasts, preparing annual budgets, and monitoring variances to ensure financial "
                "goals are met.\n"
                "Strategic Planning: Contribute to the development of financial strategies aligned with "
                "the bank's objectives, providing insights and recommendations to support "
                "decision-making at the executive level.\n"
                "Financial Reporting: Prepare and oversee the preparation of financial reports, "
                "presenting key financial information to management, stakeholders, and regulatory "
                "bodies accurately and in a timely manner.\n"
                "Process Improvement: Identify opportunities for process optimization and efficiency "
                "enhancement within financial operations, leading initiatives to streamline processes "
                "and improve overall performance."
            ),
        },
    ],

    "education": [
        {"period": "2006 - 2011", "title": "University degree | Kyrgyz-Russian Slavic University, Bishkek, Kyrgyzstan"},
        {"period": "Present", "title": "Middle Python Developer - Yandex practicum"},
        {"period": "2023", "title": "Big Data Analytics - CDAC, Noida, INDIA"},
        {"period": "2020", "title": "Java, SDET"},
        {"period": "2020", "title": "Python Programming Language"},
        {"period": "2018", "title": "ProgrammerAyimdar - Grant IT training (US embassy Democratic Comission)"},
    ],

    "skills": [
        {"label": "Java | (OOP, ORM) | Python | HTML & CSS", "percent": 97},
        {"label": "TestNG, Selenium WebDriver/Grid, Selenide, JUnit, Cucumber, BDD, Rest Assured, JDBC", "percent": 85},
        {"label": "Django, DRF, FastAPI", "percent": 80},
        {"label": "MongoDB, Postgres, MySQL, SQLite", "percent": 90},
        {"label": "Docker", "percent": 90},
        {"label": "ETL, ElasticSearch, Redis, Kafka, RabbitMQ, ZooKeeper", "percent": 60},
        {"label": "CI/CD Jenkins", "percent": 80},
        {"label": "Windows, Linux Shell Scripting", "percent": 90},
        {"label": "Git, GitHub, GitLab", "percent": 90},
        {"label": "Jira", "percent": 90},
    ],

    "languages": [
        {"label": "English", "percent": 80},
        {"label": "Russian", "percent": 100},
        {"label": "Kyrgyz", "percent": 100},
    ],

    "contact_block": {
        "phone": "+996 (555) 155551",
        "email": "info@sanzhar.com",
        "email2": "sanzhar@gmail.com",
    },
}
