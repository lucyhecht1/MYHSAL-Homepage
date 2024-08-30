from flask import Flask, render_template, request, jsonify, redirect, url_for


app = Flask(__name__)

# Variables on the server
current_id = 10
teams = [
    {
        "id": 1,
        "team-name": "Maayanot Rapids",
        "logo": "images/logos/Maayanot.png",
        "active-players": 12,
        "mission-statement": "The goals of the Maayanot athletic program are to offer a rewarding athletic experience and to develop the athletic potential of our students. Ma’ayanot athletes are encouraged to develop a sense of positive sportsmanship, integrity, values, ethics and derech eretz, and to display these qualities on and off the field. Development of leadership, personal responsibility, self-esteem, sensitivity and compassion towards others are equally important goals of the athletic program. The students learn to excel as individual players as well as members of a team.",
        "roster": ["AYELET EIZIKOVITZ | #5", "BAILA GOPIN | #44", "MIRI HOCHBERG | #11", "MICHAL JUTKOWITZ | 24", "LIANA KAHAN | #34", "SARA MIRWIS | #13", "YAEL MOTECHIN | #53", "AYELET OSTRIN | #10", "SIGAL OSTRIN | #4", "MOLLY PEARLMAN | #1", "SHIFRA PRAGER | #3", "TALI ZELKOWITZ | #20"],
        "upcoming-games": ["No upcoming games"],
        "past-games": [
            {"date": "Monday February 26, 2024", "opponent": "Frisch Cougars", "location": "@", "result": "Loss: 25-46"},
            {"date": "Monday February 12, 2024", "opponent": "FLATBUSH", "location": "@", "result": "Win: 30-28"},
            {"date": "Thursday February 1, 2024", "opponent": "Kushner Cobras", "location": "VS.", "result": "Win: 51-24"},
            {"date": "Sunday January 7, 2024", "opponent": "SAR Sting", "location": "VS.", "result": "Win: 53-41"},
            {"date": "Thursday January 4, 2024", "opponent": "Frisch Cougars", "location": "VS.", "result": "Loss: 21-74"},
            {"date": "Wednesday December 27, 2023", "opponent": "Hillel Heat", "location": "@", "result": "Win: 34-19"},
            {"date": "Thursday December 21, 2023", "opponent": "FLATBUSH", "location": "VS.", "result": "Win: 47-45"},
            {"date": "Monday December 18, 2023", "opponent": "Ramaz Rams", "location": "@", "result": "Win: 57-46"},
            {"date": "Saturday December 16, 2023", "opponent": "SAR Sting", "location": "@", "result": "Loss: 43-51"},
            {"date": "Tuesday December 5, 2023", "opponent": "Frisch Cougars", "location": "@", "result": "Loss: 52-58"}
        ],
        "home-gym": "1650 Palisade Ave, Teaneck, NJ 07666",
        "record": "8-4",
    },
    {
        "id": 2,
        "team-name": "SAR Sting",
        "logo": "images/logos/SAR.png",
        "active-players": 13,
        "mission-statement": "SAR High School is a Modern Orthodox co-educational community of learners dedicated to: Recognizing the unique needs and potential of each individual challenging each learner to move beyond his or her comfortable limits; Probing and engaging the world with humility and openness to God’s creations; Immersing themselves in a culture of learning and service as participants in the grand conversation between Torah and the world; Shaping an environment of discourse and action where mitzvot inspire respect, obligation and aspiration; Cultivating a deep respect for and devotion to Medinat Yisrael.",
        "roster": ["KIRA ALLEN | #55", "NAVA BOUSBIB | #11", "RACHELI CHAVKIN | #32", "JULIA CROOG | #25", "SAMANTHA FEIT | #0", "SYDNEY FISHKIN | #3", "JULIA HERSHMAN | #4", "GABY KALISH | #33", "GABY MERO | #44", "HADAR OHRING | #2", "CLARA ROSEN | #10", "ELIANA SMALL | #15", "LIV SOLOMON | #5"],
        "upcoming-games": ["No upcoming games"],
        "past-games": [
            {"date": "Wednesday February 7, 2024", "opponent": "North Shore Stars", "location": "VS.", "result": "Loss: 41-52"},
            {"date": "Wednesday January 31, 2024", "opponent": "Ramaz Rams", "location": "@", "result": "Win: 58-36"},
            {"date": "Tuesday January 30, 2024", "opponent": "Frisch Cougars", "location": "VS.", "result": "Loss: 47-56"},
            {"date": "Sunday January 7, 2024", "opponent": "Maayanot Rapids", "location": "@", "result": "Loss: 41-53"},
            {"date": "Tuesday December 19, 2023", "opponent": "Kushner Cobras", "location": "VS.", "result": "Win: 52-33"},
            {"date": "Saturday December 16, 2023", "opponent": "Maayanot Rapids", "location": "VS.", "result": "Win: 51-43"},
            {"date": "Tuesday December 12, 2023", "opponent": "Ramaz Rams", "location": "VS.", "result": "Win - Large Margin"},
            {"date": "Wednesday December 6, 2023", "opponent": "Kushner Cobras", "location": "@", "result": "Win: 53-27"},
            {"date": "Sunday December 3, 2023", "opponent": "Hillel Heat", "location": "VS.", "result": "Win: 66-41"},
            {"date": "Wednesday November 29, 2023", "opponent": "HANC", "location": "VS.", "result": "Win - Large Margin"}
        ],
        "home-gym": "503 West 259th Street, Bronx, NY 10471",
        "record": "9-3",
    },
    {
        "id": 3,
        "team-name": "Frisch Cougars",
        "logo": "images/logos/Frisch.png",
        "active-players": 17,
        "mission-statement": "Yeshivat Frisch is a Modern Orthodox, religious Zionist high school serving the needs of the Jewish community of Bergen County, NJ and surrounding areas. Established in 1971, Frisch provides young men and women with an exemplary education in both Judaic and general studies. We are guided by four core values: intellectual inquiry, religious growth, pursuit of passion, and kindness. In addition, we prioritize fostering meaningful relationships among students, between students and faculty, and within the wider Frisch community. In offering our students a thoughtfully-created program of formal and informal education, we aim to foster the development of every aspect of our students’ personalities and identities—intellectual, emotional, creative, communal, and religious—as they mature into young men and women whose commitment to Torah and mitzvot permeates every aspect of their lives. In the past five years, Frisch has grown from a population of 549 to over 900 students.",
        "roster": ["ALIZA BARON | #13", "JACKIE CARTER | #44", "ELIANA FISHER | #54", "ATARA FORMAN | #14", "EVELYN FRIED | #22", "DALIA HOFFER | #34", "KIRA HOFFER | #35", "ZOEY LEVY | #12", "TALIA LOWE | #32", "IZZY NADRITCH | #24", "GALIL NEUER | #1", "KAYLA NUSSBAUM | #21", "SAMANTHA PRUZANSKY | #33", "ORLI SCHARF | #42", "SARAH SILVER | #25", "LILY WURZBURGER | #23", "KAYAL YAHALOM | #10"],
        "upcoming-games": ["No upcoming games"],
        "past-games": [
            {"date": "Monday February 26, 2024", "opponent": "Maayanot Rapids", "location": "VS.", "result": "Win: 46-25"},
            {"date": "Wednesday February 14, 2024", "opponent": "HAFTR Hawks", "location": "VS.", "result": "Win: 79-30"},
            {"date": "Tuesday January 30, 2024", "opponent": "SAR Sting", "location": "@", "result": "Win: 56-47"},
            {"date": "Thursday January 4, 2024", "opponent": "Maayanot Rapids", "location": "@", "result": "Win: 74-21"},
            {"date": "Tuesday January 2, 2024", "opponent": "Kushner Cobras", "location": "VS.", "result": "Win - Large Margin"},
            {"date": "Tuesday December 19, 2023", "opponent": "Hillel Heat", "location": "VS.", "result": "Win - Large Margin"},
            {"date": "Tuesday December 5, 2023", "opponent": "Maayanot Rapids", "location": "VS.", "result": "Win: 58-52"},
            {"date": "Sunday December 3, 2023", "opponent": "SKA", "location": "@", "result": "Win: 65-54"},
            {"date": "Wednesday November 29, 2023", "opponent": "Ramaz Rams", "location": "@", "result": "Win: 61-41"},
            {"date": "Monday November 27, 2023", "opponent": "Hillel Heat", "location": "@", "result": "Win - Large Margin"}
        ],
        "home-gym": "120 W. Century Rd, Paramus, New Jersey 07652",
        "record": "12-0",
    },
    {
        "id": 4,
        "team-name": "Ramaz Rams",
        "logo": "images/logos/Ramaz.png",
        "active-players": 13,
        "mission-statement": "As a co-educational modern Orthodox Day School, Ramaz strives to educate students towards the following goals: A commitment to menschlichkeit, reflecting fineness of character, respect for others, integrity, and the centrality of chesed in all its manifestations; A commitment to Torah, mitzvot, and Ahavat Yisrael, and love and support for the State of Israel; A commitment to the pursuit of knowledge, to intellectual rigor, to scholarship, and to a life-long love of learning; Loyalty and gratitude to the United States of America, and the democratic traditions and values of our country; A sense of responsibility for the Jewish people and all humankind.",
        "roster": ["MILLI ACKERMAN | #21", "GRACE COHEN | #15", "LINDSEY FEIT | #25", "OLIVIA FERTIG | #14", "LIZZY FISHER | #12", "DAHLIA HENKIN | #11", "MOLLY HILTZIK | #24", "RAE KAPLAN | #5", "GRACE KOLLANDER | #20", "SERENA OLSHIN | #4", "EVIE ROSENFELD | #44", "LELIAH SAKHAI | #33", "LILY SCHWARTZ | #22"],
        "upcoming-games": ["No upcoming games"],
        "past-games": [
            {"date": "Wednesday February 7, 2024", "opponent": "SKA", "location": "@", "result": "Loss: 34-59"},
            {"date": "Wednesday January 31, 2024", "opponent": "SAR Sting", "location": "VS.", "result": "Loss: 36-58"},
            {"date": "Wednesday January 3, 2024", "opponent": "Hillel Heat", "location": "VS.", "result": "Win - Forfeit"},
            {"date": "Monday December 18, 2023", "opponent": "Maayanot Rapids", "location": "VS.", "result": "Loss: 46-57"},
            {"date": "Tuesday December 12, 2023", "opponent": "SAR Sting", "location": "@", "result": "Loss - Large Margin"},
            {"date": "Wednesday December 6, 2023", "opponent": "SKA", "location": "VS.", "result": "Win: 59-48"},
            {"date": "Thursday November 30, 2023", "opponent": "Kushner Cobras", "location": "@", "result": "Win: 42-28"},
            {"date": "Wednesday November 29, 2023", "opponent": "Frisch Cougars", "location": "VS.", "result": "Loss: 41-61"},
            {"date": "Tuesday November 21, 2023", "opponent": "Kushner Cobras", "location": "VS.", "result": "Win - Large Margin"},
            {"date": "Sunday November 19, 2023", "opponent": "Frisch Cougars", "location": "@", "result": "Loss - Large Margin"}
        ],
        "home-gym": "60 East 78th Street, New York, NY 10075",
        "record": "6-6",
    },
    {
        "id": 5,
        "team-name": "HAFTR Hawks",
        "logo": "images/logos/Haftr.png",
        "active-players": 12,
        "mission-statement": "At HAFTR High School, we believe in empowering the next generation of thinkers, leaders, and contributors. Here, we blend rigorous academics with deep-rooted Orthodox Jewish values, ensuring our students emerge as confident individuals ready for their future paths. We take pride in fostering an environment that nurtures individual growth while maintaining our vibrant Jewish heritage. Join us as we pave the way for tomorrow, rooted in the wisdom of our past.",
        "roster": ["TOVAH ALBOHER | #45", "ABBY FRENKEL | #23", "EMILY GORBACZ | #14", "MEGHAN GOTTFRIED | #22", "AVA GREEN | #34", "ABBI KAMMERMAN | #3", "JESSIE KURLANDER | #12", "BAILEY LEVINE | #24", "AYELET PRESTON | #1", "MEGAN SCHARF | #30", "OLIVIA WEINRIB | #21", "LILY WOLF | #33"],
        "upcoming-games": ["No upcoming games"],
        "past-games": [
            {"date": "Wednesday February 14, 2024", "opponent": "Frisch Cougars", "location": "@", "result": "Loss: 30-79"},
            {"date": "Tuesday January 30, 2024", "opponent": "FLATBUSH", "location": "VS.", "result": "Loss: 41-44"},
            {"date": "Wednesday January 3, 2024", "opponent": "Central Wildcats", "location": "@", "result": "Win: 59-36"},
            {"date": "Saturday December 30, 2023", "opponent": "HANC", "location": "@", "result": "Win: 45-32"},
            {"date": "Thursday December 28, 2023", "opponent": "FLATBUSH", "location": "@", "result": "Loss: 29-43"},
            {"date": "Wednesday December 20, 2023", "opponent": "SKA", "location": "@", "result": "Loss: 31-39"},
            {"date": "Wednesday December 13, 2023", "opponent": "North Shore Stars", "location": "VS.", "result": "Loss: 44-52"},
            {"date": "Thursday December 7, 2023", "opponent": "North Shore Stars", "location": "@", "result": "Loss: 44-58"},
            {"date": "Thursday November 30, 2023", "opponent": "SKA", "location": "VS.", "result": "Loss - Large Margin"},
            {"date": "Saturday November 11, 2023", "opponent": "HANC", "location": "VS.", "result": "Win: 55-30"}
        ],
        "home-gym": "44 Frost Lane, Lawrence, NY 11559",
        "record": "4-8",
    },
    {
        "id": 6,
        "team-name": "SKA",
        "logo": "images/logos/SKA.png",
        "active-players": 12,
        "mission-statement": "At SKA, our focus is on the development of the whole person, where we encourage our students to actualize their potential by discovering and nurturing their unique, individual talents and strengths. A full array of specialized personnel is available to students for their personal, religious and academic growth and to help students realize their dreams. Our team of social workers and school psychologists is available daily to assist students in navigating the joys and challenges of an ever-changing, fast-paced world with individual and group meetings, workshops, and parent-daughter evening events.",
        "roster": ["JULIA BERRY | #25", "ILONA BITTON | #13", "JAMIE FEDER | #22", "KAYLA GOLDBERG | #5", "SARI GROSS | #10", "ELIANNA HOLSCHENDLER | #52", "DEBBIE KOHLER | #41", "DANIELLE LEIFER | #11", "HANNAH PFEIFER | #30", "LEAH SICKLICK | #23", "REBECCA SISSER | #14", "DAPHNA STEINMETZ | #24"],
        "upcoming-games": ["No upcoming games"],
        "past-games": [
            {"date": "Tuesday February 27, 2024", "opponent": "North Shore Stars", "location": "VS.", "result": "Win: 48-46"},
            {"date": "Wednesday February 7, 2024", "opponent": "Ramaz Rams", "location": "VS.", "result": "Win: 59-34"},
            {"date": "Thursday January 4, 2024", "opponent": "North Shore Stars", "location": "VS.", "result": "Win: 50-39"},
            {"date": "Wednesday January 3, 2024", "opponent": "FLATBUSH", "location": "@", "result": "Win: 44-36"},
            {"date": "Wednesday December 27, 2023", "opponent": "Central Wildcats", "location": "VS.", "result": "Win: 43-21"},
            {"date": "Saturday December 23, 2023", "opponent": "HANC", "location": "VS.", "result": "Win - Large Margin"},
            {"date": "Wednesday December 20, 2023", "opponent": "HAFTR Hawks", "location": "VS.", "result": "Win: 39-31"},
            {"date": "Wednesday December 6, 2023", "opponent": "Ramaz Rams", "location": "@", "result": "Loss: 48-59"},
            {"date": "Sunday December 3, 2023", "opponent": "Frisch Cougars", "location": "VS.", "result": "Loss: 54-65"},
            {"date": "Thursday November 30, 2023", "opponent": "HAFTR Hawks", "location": "@", "result": "Win - Large Margin"}
        ],
        "home-gym": "291 Meadowview Avenue, Hewlett, NY 11557",
        "record": "9-3",
    },
    {
        "id": 7,
        "team-name": "Hillel Heat",
        "logo": "images/logos/Hillel.png",
        "active-players": 14,
        "mission-statement": "Hillel Yeshiva is home to enthusiastic students and faculty. We are committed to strong educational goals of academic excellence, Torah studies, the traditions of our Jewish heritage, our people, and Israel. Our strong mission and values are the foundation of our school. Our students graduate as successful young men and women ready to take on the challenges of an ever-changing world. We inspire our students to challenge, to connect and to make a difference.",
        "roster": ["ESTHER BROOCHIAN | #11", "VIVIAN DWECK | #24", "RENEE FRANCO | #23", "JANI JEMAL | #12", "PAMELA JEMAL | #14", "ROWENA KASSIN | #1", "SHELLY KASSIN | #3", "MIMI LEVY | #8", "SOPHIA LEVY | #22", "RACHEL SAADA | #10", "CHARLOTTE SAKA | #6", "RUBY SHALOM | #21", "NORMA SHAMAH | #5", "MARCELLE TORKIEH | #40"],
        "upcoming-games": ["No upcoming games"],
        "past-games": [
            {"date": "Wednesday January 3, 2024", "opponent": "Ramaz Rams", "location": "@", "result": "Loss - Forfeit"},
            {"date": "Wednesday December 27, 2023", "opponent": "Maayanot Rapids", "location": "VS.", "result": "Loss: 19-34"},
            {"date": "Thursday December 21, 2023", "opponent": "Kushner Cobras", "location": "@", "result": "Loss: 28-36"},
            {"date": "Tuesday December 19, 2023", "opponent": "Frisch Cougars", "location": "@", "result": "Loss - Large Margin"},
            {"date": "Wednesday December 13, 2023", "opponent": "Kushner Cobras", "location": "VS.", "result": "Win: 39-37"},
            {"date": "Sunday December 3, 2023", "opponent": "SAR Sting", "location": "@", "result": "Loss: 41-66"},
            {"date": "Thursday November 30, 2023", "opponent": "Maayanot Rapids", "location": "@", "result": "Loss: 24-48"},
            {"date": "Monday November 27, 2023", "opponent": "Frisch Cougars", "location": "@", "result": "Loss - Large Margin"},
            {"date": "Wednesday November 22, 2023", "opponent": "Central Wildcats", "location": "VS.", "result": "Win - Forfeit"},
            {"date": "Sunday November 19, 2023", "opponent": "HANC", "location": "@", "result": "Loss: 46-48"}
        ],
        "home-gym": "1025 Deal Rd, Ocean, NJ 07712",
        "record": "2-10",
    },
    {
        "id": 8,
        "team-name": "Kushner Cobras",
        "logo": "images/logos/Kushner.png",
        "active-players": 14,
        "mission-statement": "As a Modern Orthodox co-educational yeshiva, JKHA/RKYHS seeks to inspire students to live lives of Torah and mitzvot; to embrace secular knowledge and American democratic values; to love and serve the Jewish People; and to forge a lifelong bond with the Land and State of Israel. We aim to empower students to achieve personal excellence by teaching them how to learn, and by encouraging them to analyze, to create, and to pursue new intellectual challenges. We lead students to recognize that because we were all created in the image of God, we must treat everyone with respect and loving-kindness. We help students form strong, healthy identities, and we prepare them to take responsibility for themselves and their communities.",
        "roster": ["LEVI ADI | #3", "TALIA BANK | #24", "EMILY BAUM | #34", "SOPHIE BAUM | #30", "SOPHIE DIAMOND | #54", "ATARA FRIEDMAN | #10", "SHIREL LEVI | #31", "ARIELLE MAGID | #18", "LEVI NOA | #4", "OLIVIA RINN | #13", "EMILY TENNEBERG | #0"],
        "upcoming-games": ["No upcoming games"],
        "past-games": [
            {"date": "Thursday February 1, 2024", "opponent": "Maayanot Rapids", "location": "@", "result": "Loss: 24-51"},
            {"date": "Tuesday January 2, 2024", "opponent": "Frisch Cougars", "location": "@", "result": "Loss - Large Margin"},
            {"date": "Thursday December 21, 2023", "opponent": "Hillel Heat", "location": "VS.", "result": "Win: 36-28"},
            {"date": "Tuesday December 19, 2023", "opponent": "SAR Sting", "location": "@", "result": "Loss: 33-52"},
            {"date": "Sunday December 17, 2023", "opponent": "North Shore Stars", "location": "VS.", "result": "Loss - Large Margin"},
            {"date": "Wednesday December 13, 2023", "opponent": "Hillel Heat", "location": "@", "result": "Loss: 37-39"},
            {"date": "Wednesday December 6, 2023", "opponent": "SAR Sting", "location": "VS.", "result": "Loss: 27-53"},
            {"date": "Thursday November 30, 2023", "opponent": "Ramaz Rams", "location": "@", "result": "Loss: 28-42"},
            {"date": "Tuesday November 21, 2023", "opponent": "Ramaz Rams", "location": "@", "result": "Loss - Large Margin"},
            {"date": "Thursday November 9, 2023", "opponent": "Central Wildcats", "location": "@", "result": "Win: 50-41"}
        ],
        "home-gym": "110 South Orange Ave, Livingston, NJ 07039",
        "record": "2-10",
    },
    {
        "id": 9,
        "team-name": "Central Wildcats",
        "logo": "images/logos/Central.png",
        "active-players": 10,
        "mission-statement": "Our distinguished history in Jewish education dates back to 1948. Our vision is as innovative and creative as the 21st century itself. The spiritual and academic life of Yeshiva University High School for Girls/Central is built upon the philosophy of Torah U’Madda L’chatchila. We believe that the synthesis of Jewish law and life and the wisdom of world civilization results in a heightened and enriched Judaism. Our mission directs our students to be knowledgeable, halachically committed Jews and broadly educated, intellectually curious, and caring members of society. As life-long learners, our students develop a personal devotion to G-d, Torah learning, integrity and commitment to ethical behavior. Identification with the destiny of our fellow Jews around the world, loyalty to Eretz Yisrael, and recognition of the modern State of Israel as the spiritual homeland of the Jewish people and the fulfillment of a religious Zionist vision are all cornerstones of our educational program. Our commitment to Torah U’Madda requires students to pursue all academic studies with the intent of achieving a greater understanding of the world, reaching for personal academic achievement, and making a lasting difference in our community.",
        "roster": ["SAMANTHA BURGER | #4", "HANNAH FINK | #32", "MELANIE GAVRIELOV | #22", "MICHAL KATZ | #5", "AVIVA KESSOCK | #3", "ELIANA LEITNER | #10", "AVA RESCHKE | #15", "SHIREL SHIVAMEHR | #54", "REBECCA YUNATAN | #31", "CHANNAH YUROVSKY | 11"],
        "upcoming-games": ["No upcoming games"],
        "past-games": [
            {"date": "Wednesday January 3, 2024", "opponent": "HAFTR Hawks", "location": "VS.", "result": "Loss: 36-59"},
            {"date": "Wednesday December 27, 2023", "opponent": "SKA", "location": "@", "result": "Loss: 21-43"},
            {"date": "Wednesday December 20, 2023", "opponent": "HANC", "location": "VS.", "result": "Loss: 36-51"},
            {"date": "Saturday December 16, 2023", "opponent": "HANC", "location": "@", "result": "Loss: 33-49"},
            {"date": "Monday December 4, 2023", "opponent": "FLATBUSH", "location": "@", "result": "Loss - Large Margin"},
            {"date": "Monday November 27, 2023", "opponent": "North Shore Stars", "location": "@", "result": "Loss - Large Margin"},
            {"date": "Wednesday November 22, 2023", "opponent": "Hillel Heat", "location": "@", "result": "Loss - Forfeit"},
            {"date": "Monday November 20, 2023", "opponent": "North Shore Stars", "location": "VS.", "result": "Loss - Large Margin"},
            {"date": "Thursday November 9, 2023", "opponent": "Kushner Cobras", "location": "VS.", "result": "Loss: 41-50"},
            {"date": "Wednesday November 1, 2023", "opponent": "HAFTR Hawks", "location": "@", "result": "Loss - Large Margin"}
        ],
        "home-gym": "86-86 Palo Alto Street, Holliswood, NY 11423",
        "record": "0-12",
    },
    {
        "id": 10,
        "team-name": "North Shore Stars",
        "logo": "images/logos/Northshore.png",
        "active-players": 10,
        "mission-statement": "The North Shore Hebrew Academy High School strives, first and foremost, to combine the best of Jewish and General studies into an integrated, well-rounded, and personally rewarding education for each of its students. It is our hope that by offering a first-rate program in all areas of our Jewish and world heritage, from Torah, Talmud, Hebrew, and Bible classes, to literature, art, science, and athletics, we will help our students realize their fullest potential. In doing so, they will gain a greater appreciation for learning and their own self-worth. These goals proceed directly from the principles that all knowledge is a reflection of God’s infinite wisdom and all humanity the manifestation of His image.",
        "roster": ["SOFIA ASHER | #13", "REBECCA GOLYAN | #24", "DILLAN HAGHIGHAT | #40", "SOPHIA HAJIBAI | #10", "ALEXA HAJIBAY | #5", "ABBY IJADI | #11", "SHIREL KASHIMALLAK | #1", "MICHAELA KOVAN | #22", "DINA LEVIAN | #30", "SYMONE YAAKOVZADEH | #23"],
        "upcoming-games": ["No upcoming games"],
        "past-games": [
            {"date": "Tuesday February 27, 2024", "opponent": "SKA", "location": "@", "result": "Loss: 46-48"},
            {"date": "Wednesday February 7, 2024", "opponent": "SAR Sting", "location": "@", "result": "Win: 52-41"},
            {"date": "Tuesday January 30, 2024", "opponent": "HANC", "location": "@", "result": "Win: 81-39"},
            {"date": "Thursday January 4, 2024", "opponent": "SKA", "location": "@", "result": "Loss: 39-50"},
            {"date": "Sunday December 17, 2023", "opponent": "Kushner Cobras", "location": "@", "result": "Win - Large Margin"},
            {"date": "Wednesday December 13, 2023", "opponent": "HAFTR Hawks", "location": "@", "result": "Win: 52-44"},
            {"date": "Tuesday December 12, 2023", "opponent": "FLATBUSH", "location": "VS.", "result": "Loss: 43-53"},
            {"date": "Thursday December 7, 2023", "opponent": "HAFTR Hawks", "location": "VS.", "result": "Win: 58-44"},
            {"date": "Tuesday December 5, 2023", "opponent": "HANC", "location": "VS.", "result": "Win: 72-59"},
            {"date": "Wednesday November 29, 2023", "opponent": "Maayanot Rapids", "location": "VS.", "result": "Win: 65-54"}
        ],
        "home-gym": "400 North Service Rd, Great Neck, NY 11020",
        "record": "8-4",
    },
]
with app.test_request_context():
    for team in teams:
        team["logo"] = url_for('static', filename=team['logo'])


@app.route('/')
def home():
    # Select teams with IDs 1, 2, and 3 for the homepage
    featured_teams = [team for team in teams if team["id"] in (1, 2, 3)]
    return render_template('welcome.html', featured_teams=featured_teams)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').strip().lower()
    if query:
        search_results = [team for team in teams if any(query in field.lower() for field in [team["team-name"], team["home-gym"], " ".join(team["roster"])])]
        num_results = len(search_results)
        return render_template('search_results.html', query=query, search_results=search_results, num_results=num_results)
    else:
        return render_template('search_results.html', query=query, search_results=[], num_results=0)

@app.route('/search_results')
def show_search_results():
    query = request.args.get('q', '').strip()
    search_results = request.json
    return render_template('search_results.html', query=query, search_results=search_results)

@app.route('/view/<int:team_id>')
def view_team(team_id):
    global teams
    # Find the team by ID
    dict_teams= {} 
    for team in teams:
       dict_teams[team["team-name"]] = team["id"]
    team = next((team for team in teams if team["id"] == team_id), None)
    if team:
        return render_template('team_detail.html', team=team, dict_teams=dict_teams)
    else:
        return 'Team not found', 404

@app.route('/add', methods=['GET', 'POST'])
def add_team():
    if request.method == 'POST':
        # Get data from the form
        team_name = request.form.get('team_name')
        logo = request.form.get('logo')
        active_players = int(request.form.get('active_players'))
        mission_statement = request.form.get('mission_statement')
        roster = request.form.get('roster').split(',')
        upcoming_games = request.form.get('upcoming_games').split(",")
        
        home_gym = request.form.get('home_gym')
        record = request.form.get('record')

        # Some crazzyy business for past 10 games, but worth it!!
        date1 = request.form.get('date1')
        opponent1 = request.form.get('opponent1')
        location1 = request.form.get('location1')
        result1 = request.form.get('result1')

        date2 = request.form.get('date2')
        opponent2 = request.form.get('opponent2')
        location2 = request.form.get('location2')
        result2 = request.form.get('result2')

        date3 = request.form.get('date3')
        opponent3 = request.form.get('opponent3')
        location3 = request.form.get('location3')
        result3 = request.form.get('result3')

        date4 = request.form.get('date4')
        opponent4 = request.form.get('opponent4')
        location4 = request.form.get('location4')
        result4 = request.form.get('result4')

        date5 = request.form.get('date5')
        opponent5 = request.form.get('opponent5')
        location5 = request.form.get('location5')
        result5 = request.form.get('result5')

        date6 = request.form.get('date6')
        opponent6 = request.form.get('opponent6')
        location6 = request.form.get('location6')
        result6 = request.form.get('result6')

        date7 = request.form.get('date7')
        opponent7 = request.form.get('opponent7')
        location7 = request.form.get('location7')
        result7 = request.form.get('result7')

        date8 = request.form.get('date8')
        opponent8 = request.form.get('opponent8')
        location8 = request.form.get('location8')
        result8 = request.form.get('result8')

        date9 = request.form.get('date9')
        opponent9 = request.form.get('opponent9')
        location9 = request.form.get('location9')
        result9 = request.form.get('result9')

        date10 = request.form.get('date10')
        opponent10 = request.form.get('opponent10')
        location10 = request.form.get('location10')
        result10 = request.form.get('result10')

        past_games = [{"date": date1, "opponent": opponent1, "location": location1, "result": result1},
                      {"date": date2, "opponent": opponent2, "location": location2, "result": result2},
                      {"date": date3, "opponent": opponent3, "location": location3, "result": result3},
                      {"date": date4, "opponent": opponent4, "location": location4, "result": result4},
                      {"date": date5, "opponent": opponent5, "location": location5, "result": result5},
                      {"date": date6, "opponent": opponent6, "location": location6, "result": result6},
                      {"date": date7, "opponent": opponent7, "location": location7, "result": result7},
                      {"date": date8, "opponent": opponent8, "location": location8, "result": result8},
                      {"date": date9, "opponent": opponent9, "location": location9, "result": result9},
                      {"date": date10, "opponent": opponent10, "location": location10, "result": result10} ]

        errors = []
        if not team_name.strip():
            errors.append("Team name cannot be empty.")

        # If there are errors, return them to the client
        if errors:
            return jsonify({'success': False, 'errors': errors}), 400

        # Save the new data
        global current_id
        current_id += 1
        new_team_id = current_id
        new_team = {
            "id": current_id,
            "team-name": team_name,
            "logo": logo,
            "active-players": active_players,
            "mission-statement": mission_statement,
            "roster": roster,
            "upcoming-games": upcoming_games,
            "past-games": past_games,
            "home-gym": home_gym,
            "record": record
        }
        teams.append(new_team)
        return jsonify({'success': True, 'id': new_team_id})

    return render_template('add_team.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_team(id):
    global teams
    if request.method == 'GET':
        team = next((team for team in teams if team["id"] == id), None)
        if team:
            return render_template('edit_team.html', team=team, team_id=id)
        else:
            return "Team not found", 404
    elif request.method == 'POST':
        # Handle form submission to update team data
        team_name = request.form.get('team-name')
        logo = request.form.get('logo')
        active_players = request.form.get('active-players')  
        mission_statement = request.form.get('mission-statement') 
        roster = request.form.get('roster')
        upcoming_games = request.form.get('upcoming-games')

        home_gym = request.form.get('home-gym')
        record = request.form.get('record')

        # Some crazzyy business for past 10 games, but worth it!!
        date1 = request.form.get('date1')
        opponent1 = request.form.get('opponent1')
        location1 = request.form.get('location1')
        result1 = request.form.get('result1')

        date2 = request.form.get('date2')
        opponent2 = request.form.get('opponent2')
        location2 = request.form.get('location2')
        result2 = request.form.get('result2')

        date3 = request.form.get('date3')
        opponent3 = request.form.get('opponent3')
        location3 = request.form.get('location3')
        result3 = request.form.get('result3')

        date4 = request.form.get('date4')
        opponent4 = request.form.get('opponent4')
        location4 = request.form.get('location4')
        result4 = request.form.get('result4')

        date5 = request.form.get('date5')
        opponent5 = request.form.get('opponent5')
        location5 = request.form.get('location5')
        result5 = request.form.get('result5')

        date6 = request.form.get('date6')
        opponent6 = request.form.get('opponent6')
        location6 = request.form.get('location6')
        result6 = request.form.get('result6')

        date7 = request.form.get('date7')
        opponent7 = request.form.get('opponent7')
        location7 = request.form.get('location7')
        result7 = request.form.get('result7')

        date8 = request.form.get('date8')
        opponent8 = request.form.get('opponent8')
        location8 = request.form.get('location8')
        result8 = request.form.get('result8')

        date9 = request.form.get('date9')
        opponent9 = request.form.get('opponent9')
        location9 = request.form.get('location9')
        result9 = request.form.get('result9')

        date10 = request.form.get('date10')
        opponent10 = request.form.get('opponent10')
        location10 = request.form.get('location10')
        result10 = request.form.get('result10')

        past_games = [{"date": date1, "opponent": opponent1, "location": location1, "result": result1},
                      {"date": date2, "opponent": opponent2, "location": location2, "result": result2},
                      {"date": date3, "opponent": opponent3, "location": location3, "result": result3},
                      {"date": date4, "opponent": opponent4, "location": location4, "result": result4},
                      {"date": date5, "opponent": opponent5, "location": location5, "result": result5},
                      {"date": date6, "opponent": opponent6, "location": location6, "result": result6},
                      {"date": date7, "opponent": opponent7, "location": location7, "result": result7},
                      {"date": date8, "opponent": opponent8, "location": location8, "result": result8},
                      {"date": date9, "opponent": opponent9, "location": location9, "result": result9},
                      {"date": date10, "opponent": opponent10, "location": location10, "result": result10} ]

        # Update the team data by creating a dict with the keys
        teams[id - 1] = {
            "id": id,
            "team-name": team_name, 
            "logo": logo,
            "active-players": active_players, 
            "mission-statement": mission_statement,
            "roster": roster.split(","), 
            "upcoming-games": upcoming_games.split(","),
            "past-games": past_games,  
            "home-gym": home_gym, 
            "record": record
        }
        # Redirect to the view page for the edited team
        return redirect(url_for('view_team', team_id=id))
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)