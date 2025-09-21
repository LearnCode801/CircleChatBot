# Circle Chatbot
## 🎥 Demo Video

**Click to watch the demo:** [Circle Chatbot](https://drive.google.com/file/d/1kAJjkmc476nPm8HNkAvzGTN_YPevHOfD/view?usp=sharing)

## Overview

The Circle Chatbot is Startup Recommendation System which designed to provide insightful and relevant recommendations to users based on their startup ideas. Users can input detailed descriptions and details about their proposed startup, and the system will match these with a database of 4361 startups to provide helpful data and insights.

## Features

- **Detailed Query Handling**: Users can input comprehensive descriptions of their startup ideas.
- **Contextual Matching**: The system matches user input with a rich database of startup information.
- **Relevant Recommendations**: Provides users with relevant data about existing startups similar to their idea.
- **User-Friendly Responses**: Clear and concise responses to user queries, focusing on startups and business information.

## Data

The system uses the following data fields for each startup:
- `company_id`
- `company_name`
- `short_description`
- `long_description`
- `batch`
- `status`
- `tags`
- `location`
- `country`
- `year_founded`
- `num_founders`
- `founders_names`
- `team_size`
- `website`
- `cb_url` (Crunchbase URL)
- `linkedin_url`

## Usage

### Example Usage

Users can query the system by providing their startup idea and receiving information about similar existing startups. For example:

```plaintext
Question: "I want to start a social media platform for pet owners to share and connect. What similar startups are there?"
```

The system will then provide details on relevant startups based on the context of the user's query.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/LearnCode801/CircleChatBot.git
    ```

2. Install dependencies:
    ```sh
    cd startup-recommendation-system
    pip install -r requirements.txt
    ```

3. Run the application:
    ```sh
    python app.py
    ```

## Contribution

We welcome contributions to improve the Startup Recommendation System. Please fork the repository and submit pull requests for any enhancements or bug fixes.


## Contact

For any questions or feedback, please contact [Muhammad Talha] at [muhammadtalhaawan801@gmail.com].

---

This README file should provide a clear and comprehensive overview of your project, guiding users through its purpose, usage, and contribution guidelines.

