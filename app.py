import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Online Internship Management Portal",
    page_icon="🎓",
    layout="wide"
)

# ---------------- SESSION DATA ----------------
if "internships" not in st.session_state:
    st.session_state.internships = [
        {
            "title": "Python Developer Intern",
            "company": "ABC Technologies",
            "location": "Hyderabad",
            "duration": "3 Months",
            "skills": "Python, SQL",
            "description": "Work on Python-based web applications."
        },
        {
            "title": "Web Development Intern",
            "company": "XYZ Solutions",
            "location": "Bangalore",
            "duration": "6 Months",
            "skills": "HTML, CSS, JavaScript",
            "description": "Develop and maintain modern web applications."
        },
        {
            "title": "Data Science Intern",
            "company": "DataTech",
            "location": "Remote",
            "duration": "4 Months",
            "skills": "Python, Pandas, Machine Learning",
            "description": "Work on data analysis and machine learning projects."
        }
    ]

if "applications" not in st.session_state:
    st.session_state.applications = []


# ---------------- SIDEBAR ----------------
st.sidebar.title("🎓 Internship Portal")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "👨‍🎓 Student",
        "🏢 Company",
        "📋 Internships",
        "📊 Applications",
        "🔐 Admin"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("Online Internship Management System")


# =========================================================
# HOME
# =========================================================

if page == "🏠 Home":

    st.title("🎓 Online Internship Management Portal")

    st.subheader("Welcome to the Internship Management System")

    st.write(
        "A simple platform for students to find internships, "
        "companies to post opportunities, and administrators "
        "to manage the entire system."
    )

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "👨‍🎓 Students",
            "120"
        )

    with col2:
        st.metric(
            "🏢 Companies",
            "25"
        )

    with col3:
        st.metric(
            "📋 Internships",
            len(st.session_state.internships)
        )

    st.markdown("---")

    st.subheader("✨ Portal Features")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("""
        ### 👨‍🎓 Student
        - Student registration
        - Student login
        - Search internships
        - Apply for internships
        - Track applications
        """)

    with c2:
        st.markdown("""
        ### 🏢 Company
        - Company registration
        - Company login
        - Post internships
        - View applications
        - Manage opportunities
        """)


# =========================================================
# STUDENT
# =========================================================

elif page == "👨‍🎓 Student":

    st.title("👨‍🎓 Student Portal")

    student_action = st.selectbox(
        "Select Action",
        [
            "Register",
            "Login"
        ]
    )

    # ---------------- STUDENT REGISTER ----------------

    if student_action == "Register":

        st.subheader("📝 Student Registration")

        col1, col2 = st.columns(2)

        with col1:
            name = st.text_input("Full Name")
            email = st.text_input("Email")
            phone = st.text_input("Phone Number")

        with col2:
            college = st.text_input("College / University")
            course = st.text_input("Course")
            password = st.text_input(
                "Password",
                type="password"
            )

        if st.button(
            "Register Student",
            type="primary"
        ):

            if name and email and college and course and password:

                st.success(
                    f"Registration successful! Welcome {name}."
                )

            else:

                st.error(
                    "Please fill all required fields."
                )

    # ---------------- STUDENT LOGIN ----------------

    elif student_action == "Login":

        st.subheader("🔐 Student Login")

        email = st.text_input("Email")
        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button(
            "Login",
            type="primary"
        ):

            if email and password:

                st.success(
                    "Student login successful!"
                )

            else:

                st.error(
                    "Please enter email and password."
                )


# =========================================================
# COMPANY
# =========================================================

elif page == "🏢 Company":

    st.title("🏢 Company Portal")

    company_action = st.selectbox(
        "Select Action",
        [
            "Register Company",
            "Login",
            "Post Internship"
        ]
    )

    # ---------------- COMPANY REGISTER ----------------

    if company_action == "Register Company":

        st.subheader("📝 Company Registration")

        col1, col2 = st.columns(2)

        with col1:
            company_name = st.text_input(
                "Company Name"
            )

            company_email = st.text_input(
                "Company Email"
            )

            phone = st.text_input(
                "Phone Number"
            )

        with col2:

            website = st.text_input(
                "Company Website"
            )

            company_password = st.text_input(
                "Password",
                type="password"
            )

        if st.button(
            "Register Company",
            type="primary"
        ):

            if (
                company_name
                and company_email
                and company_password
            ):

                st.success(
                    "Company registered successfully!"
                )

            else:

                st.error(
                    "Please fill all required fields."
                )

    # ---------------- COMPANY LOGIN ----------------

    elif company_action == "Login":

        st.subheader("🔐 Company Login")

        email = st.text_input(
            "Company Email"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button(
            "Login",
            type="primary"
        ):

            if email and password:

                st.success(
                    "Company login successful!"
                )

            else:

                st.error(
                    "Please enter email and password."
                )

    # ---------------- POST INTERNSHIP ----------------

    elif company_action == "Post Internship":

        st.subheader("📢 Post New Internship")

        title = st.text_input(
            "Internship Title"
        )

        company = st.text_input(
            "Company Name"
        )

        location = st.text_input(
            "Location"
        )

        duration = st.text_input(
            "Duration"
        )

        skills = st.text_input(
            "Required Skills"
        )

        description = st.text_area(
            "Internship Description"
        )

        if st.button(
            "Post Internship",
            type="primary"
        ):

            if (
                title
                and company
                and location
                and duration
                and skills
            ):

                new_internship = {
                    "title": title,
                    "company": company,
                    "location": location,
                    "duration": duration,
                    "skills": skills,
                    "description": description
                }

                st.session_state.internships.append(
                    new_internship
                )

                st.success(
                    "Internship posted successfully!"
                )

            else:

                st.error(
                    "Please fill all required fields."
                )


# =========================================================
# INTERNSHIPS
# =========================================================

elif page == "📋 Internships":

    st.title("📋 Available Internships")

    search = st.text_input(
        "🔍 Search internships",
        placeholder="Example: Python"
    )

    st.markdown("---")

    found = False

    for index, internship in enumerate(
        st.session_state.internships
    ):

        search_text = (
            internship["title"]
            + internship["company"]
            + internship["skills"]
            + internship["location"]
        ).lower()

        if search.lower() in search_text:

            found = True

            with st.container(border=True):

                st.subheader(
                    f"💼 {internship['title']}"
                )

                col1, col2 = st.columns(2)

                with col1:

                    st.write(
                        f"🏢 **Company:** "
                        f"{internship['company']}"
                    )

                    st.write(
                        f"📍 **Location:** "
                        f"{internship['location']}"
                    )

                    st.write(
                        f"⏳ **Duration:** "
                        f"{internship['duration']}"
                    )

                with col2:

                    st.write(
                        f"🛠️ **Skills:** "
                        f"{internship['skills']}"
                    )

                    st.write(
                        f"📝 **Description:** "
                        f"{internship['description']}"
                    )

                if st.button(
                    "Apply Now",
                    key=f"apply_{index}"
                ):

                    application = {
                        "internship": internship["title"],
                        "company": internship["company"],
                        "student": "Current Student",
                        "status": "Pending"
                    }

                    st.session_state.applications.append(
                        application
                    )

                    st.success(
                        "Application submitted successfully!"
                    )

    if not found:

        st.warning(
            "No internships found."
        )


# =========================================================
# APPLICATIONS
# =========================================================

elif page == "📊 Applications":

    st.title("📊 My Applications")

    if len(st.session_state.applications) == 0:

        st.info(
            "You have not applied for any internship yet."
        )

    else:

        for index, application in enumerate(
            st.session_state.applications
        ):

            with st.container(border=True):

                st.subheader(
                    f"💼 {application['internship']}"
                )

                st.write(
                    f"🏢 Company: "
                    f"{application['company']}"
                )

                st.write(
                    f"👨‍🎓 Student: "
                    f"{application['student']}"
                )

                status = application["status"]

                if status == "Selected":

                    st.success(
                        f"Status: {status}"
                    )

                elif status == "Rejected":

                    st.error(
                        f"Status: {status}"
                    )

                else:

                    st.warning(
                        f"Status: {status}"
                    )


# =========================================================
# ADMIN
# =========================================================

elif page == "🔐 Admin":

    st.title("🔐 Admin Dashboard")

    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "👨‍🎓 Students",
            "120"
        )

    with col2:

        st.metric(
            "🏢 Companies",
            "25"
        )

    with col3:

        st.metric(
            "📋 Internships",
            len(st.session_state.internships)
        )

    with col4:

        st.metric(
            "📝 Applications",
            len(st.session_state.applications)
        )

    st.markdown("---")

    st.subheader("📋 Internship List")

    for internship in st.session_state.internships:

        st.write(
            f"**{internship['title']}** — "
            f"{internship['company']} — "
            f"{internship['location']}"
        )

    st.markdown("---")

    st.subheader("📝 Applications")

    if len(st.session_state.applications) == 0:

        st.info("No applications yet.")

    else:

        for application in st.session_state.applications:

            st.write(
                f"👨‍🎓 {application['student']} | "
                f"💼 {application['internship']} | "
                f"🏢 {application['company']} | "
                f"Status: {application['status']}"
            )