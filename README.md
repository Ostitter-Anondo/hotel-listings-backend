<h1>Hotel Listings Backend Built On Django + DjangoORM</h1>
<hr><p>This is the backend repo for the "Technometrics: Junior Software Engineer Assessment".</p>
<p>This project was built using Django. Database connections are handled using DjangoORM.</p><h2>General Information</h2>
<hr><ul>
<li>It's a very unimpressive Django project thing</li>
</ul><ul>
<li>It solves literally no problems whatsoever</li>
</ul><ul>
<li>This exists solely as a proof that I can use Django</li>
</ul><h2>Technologies Used</h2>
<hr><ul>
<li>HTML</li>
</ul><ul>
<li>Django</li>
</ul><ul>
<li>SQLite</li>
</ul><h2>Features</h2>
<hr><ul>
<li>For now it can only serve GET requests and return JSON endpoints as a response</li>
</ul><h2>Setup</h2>
<hr><p>To start with, activate your desired (preferably fresh) virtual environment with python. If you do not have python, you can get it from https://www.python.org/downloads/</p><h5>Steps</h5><ul>
<li>Install Django (mac/linux)</li>
</ul><p><code>python -m pip install Django</code></p><ul>
<li>Install Django (windows)</li>
</ul><p><code>py -m pip install Django</code></p><ul>
<li>Install CORS Headers</li>
</ul><p><code>python -m pip install django-cors-headers</code></p><ul>
<li>Install Jinja (I think I used it for the landing page, not sure tho)</li>
</ul><p><code>pip install Jinja2</code></p>
<ul>
  <li>at the very bottom of demo/settings.py, remember to add the url your front end is being hosted at. currently it only has the default url for vite+react</li>
</ul>
<li>django superuser credentials:</li>
</ul><p><code>username: "admin", password: "admin"</code></p>

<hr><p>Partially Complete (or you can just be mean and say incomplete, I don't mind, I think), because this is my first ever Django project, I don't yet know how to handle POST/PUT requests, and I am not sure how to deal with secure password storage, so I decided not to add authentication.</p><h2>Improvements</h2>
<hr><ul>
<li>Add a basic auth system</li>
</ul><ul>
<li>Store bookmarks by user profile, rather than locally</li>
</ul><h2>Features that can be added</h2>
<hr><ul>
<li>JWT based secure authentication</li>
</ul><ul>
<li>Making use of COOKIES somehow</li>
</ul><h2>Acknowledgement</h2>
<hr><ul>
<li>This project was built entirely as an assessment of my skills</li>
</ul><ul>
<li>I literally watched a 20 minute Django tutorial before starting it: https://www.youtube.com/watch?v=nGIg40xs9e4</li>
</ul><ul>
<li>Mostly myself, but also Sanjib bhai for giving me this opportunity</li>
</ul><h2>Contact</h2>
<hr><p><span style="margin-right: 30px;"></span><a href="https://www.linkedin.com/in/jawad-ibn-mamoon/"><img style="width: 10%;" target="_blank" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg"></a><span style="margin-right: 30px;"></span><a href="https://github.com/Ostitter-Anondo"><img style="width: 10%;" target="_blank" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg"></a><span style="margin-right: 30px;"></span><a href="https://www.facebook.com/ostitter.anondo"><img style="width: 10%;" target="_blank" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/facebook/facebook-original.svg"></a></p>
# hotel-listings-backend
