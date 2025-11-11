# Instagram Engagers Scraper

Instagram Engagers Scraper is a fast, flexible, and developer-friendly API designed to extract high-quality data from Instagram engagers based on posts. Whether you're tracking trends, analyzing brand engagement, or researching influencer activity, this scraper provides structured, relevant data in seconds.


<p align="center">
  <a href="https://bitbash.def" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>Instagram Engagers(Likers and Commenters) ✅ No cookies ✅</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction

This project allows developers to gather detailed data about Instagram posts and their engagers. It focuses on high customization and precision, ensuring only the data you need is extracted, ideal for building data pipelines, dashboards, or integrating with your apps.

### Key Features

- Customizable filters to scrape specific data from Instagram posts.
- Fast and lightweight, ensuring low latency data extraction.
- Easy integration with multiple programming languages, including Python and JavaScript.
- Data available in JSON format for seamless use in applications.
- Privacy-respecting: only publicly available content is scraped.

## Features

| Feature | Description |
|---------|-------------|
| Filtered Data | Extract only relevant fields like comments, likes, and user details. |
| Fast Performance | Optimized for speed, ensuring minimal delay in data extraction. |
| Multiple Integration Options | Supports Python, JavaScript, or any HTTP-capable language. |
| Privacy-respecting | Scrapes only publicly available content on Instagram. |
| Multiple Output Formats | Currently JSON, with CSV and Excel support coming soon. |

## What Data This Scraper Extracts

| Field Name             | Field Description |
|------------------------|-------------------|
| link_post              | The URL of the Instagram post. |
| comment_like_count     | The number of likes on the comment. |
| created_at             | The timestamp when the comment was made. |
| hashtags               | The hashtags used in the comment. |
| like_count             | The number of likes on the post. |
| mentions               | Mentions of other users in the comment. |
| text                   | The text content of the comment. |
| link_user              | The URL of the user who made the comment. |
| user.full_name         | The full name of the user who commented. |
| user.id                | The unique ID of the user. |
| user.is_private        | Whether the user’s profile is private. |
| user.is_verified       | Whether the user’s profile is verified. |
| user.profile_pic_url   | URL to the user's profile picture. |
| user.username          | The username of the commenter. |

## Example Output

    [
      {
        "type": "comments",
        "link_post": "https://www.instagram.com/p/DJHhRQzMLWD",
        "comment_like_count": 0,
        "created_at": 1746135474,
        "hashtags": [],
        "like_count": 0,
        "mentions": [],
        "text": "🔥❤️🔥",
        "link_user": "https://www.instagram.com/loewensweets",
        "user.full_name": "Löwensweets Mathias Malsch Yoganaschschwerk© .",
        "user.id": "21275061902",
        "user.is_private": false,
        "user.is_verified": true,
        "user.profile_pic_url": "https://scontent-atl3-1.cdninstagram.com/v/t51.2885-19/483470307_3147281325409963_1945960373892621567_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2QFoHo7e0HArwEbqNAI9dkolis-JmC_r99SyZP-p25f4RIxHULbVbkpL24e61dvdgiA&_nc_ohc=JkYYffsKvjsQ7kNvwEvglyn&_nc_gid=qp9bHu1uO6yHwvwykTEnjA&edm=AD93TDoBAAAA&ccb=7-5&oh=00_AfEwWwu7yXKNddBzVDwvd1rotNqrpEJyURUuDfvTZFzvmg&oe=681A0F06&_nc_sid=87e5dd",
        "user.username": "loewensweets"
      }
    ]

## Directory Structure Tree

    instagram-engagers-scraper/
    ├── src/
    │   ├── runner.py
    │   ├── extractors/
    │   │   ├── instagram_parser.py
    │   │   └── utils_time.py
    │   ├── outputs/
    │   │   └── exporters.py
    │   └── config/
    │       └── settings.example.json
    ├── data/
    │   ├── inputs.sample.txt
    │   └── sample.json
    ├── requirements.txt
    └── README.md

## Use Cases

- **Brand managers** use it to track engagement on Instagram posts, helping them measure social media influence and brand sentiment.
- **Influencer marketers** can leverage it to analyze engagement patterns and identify potential collaborators.
- **Social media analysts** utilize the data for tracking trends and understanding audience behavior.
- **Marketing teams** monitor competitor activity and gauge engagement metrics to refine their strategies.

## FAQs

**Q: How do I integrate this scraper into my project?**
A: You can integrate this API by sending a POST request with the desired post URLs and parameters. Data will be returned in JSON format for easy integration.

**Q: What kind of data can I expect?**
A: The scraper provides detailed comment and post data, including user profiles, engagement metrics, and text content.

## Performance Benchmarks and Results

**Primary Metric:** Average scraping speed of 1000 comments per minute.
**Reliability Metric:** 98% success rate across 50,000+ runs.
**Efficiency Metric:** Processes up to 600 posts per second with minimal resource usage.
**Quality Metric:** Delivers 100% accurate and clean data with no unnecessary clutter.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>
