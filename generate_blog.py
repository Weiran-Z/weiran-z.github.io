import glob
import markdown
from datetime import datetime


beginning = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog Article</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville&family=Lora:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">    
    <link rel="icon" type="image/x-icon" href="../pics/favicon.ico">
    <script src="https://cdn.jsdelivr.net/npm/@webcomponents/webcomponentsjs@2/webcomponents-loader.min.js"></script>
    <script type="module" src="https://cdn.jsdelivr.net/gh/zerodevx/zero-md@1/src/zero-md.min.js"></script> 
    <link rel="stylesheet" href="../styles.css">
</head>
<body class="blog">
    <div class="bg-text">Weiran Zhang</div>
    <div class="header-box">  
        <div><a href="/" class="item">Home</a></div>
        <!-- <div><a href="#" class="item">Portfolio</a></div> -->
        <div><a href="/blog" class="item">Blog</a></div>
        <div><a href="/resume" class="item">Resume</a></div>
    </div>
    <div class="container">
    """

end = """
    </div>
</body>
</html>
"""

separator = """
<div class="separator">
  <div class="black-bar"></div>
  <div class="white-space">
    <span class="emoji">🐷&nbsp;🐷&nbsp;🐷</span>
  </div>
  <div class="black-bar"></div>
</div>
"""

with open("blog.html", "w") as f:
    f.write(beginning)
    all_files = []
    for mdfilename in glob.glob('articles/*.md'):
        with open(mdfilename, "r") as md:
            article = md.readlines()
            date_string = article[2].strip('\n')
            all_files.append((mdfilename, date_string))
            
    for mdfilename,_ in sorted(all_files, key= lambda x: x[1], reverse=True):
        with open(mdfilename, "r") as md:
            article = md.readlines()
            title = article[1].strip('\n')
            date_string = article[2].strip('\n')
            date_object = datetime.strptime(date_string, "%Y-%m-%d")
            formatted_date = date_object.strftime("%B %d, %Y")
            date = formatted_date
            content = markdown.markdown("".join(article))
            middle = f"""<details>
                    <summary>
                        <h2>{title}</h2>
                        <div class="post-meta">Posted on {date}</div>
                    </summary>
                    <article>
                        {content}
                        {separator}
                    </article>
                </details>    """
            f.write(middle)
            
    f.write(end)
