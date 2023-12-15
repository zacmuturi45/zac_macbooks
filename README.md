<h1>Zac’s Macbook Shop</h1>
<h2>A CLI-Based Shipment Tracking & Inventory System</h2>


<h2>ABOUT</h2>
<p>Zac's Macbook Shop is a CLI based application made for Mr. Zac Muturi's Macbook Shop. The application tracks inventory received and manages sales data.</p>


<h2>SETUP</h2>
<ol>
<li>Create a folder where you will clone the app data.</li>
<li>Copy the link to clone the app files and cd into your new folder to clone to your local machine</li>
<li>cd into the cloned directory and run <code>pipenv install && pipenv shell</code></li>
<li>cd into the src directory then run <code>python3 cli.py</code></li>
<li>Congratulations, you can now interact with the CLI to use the app</li>
</ol>

<h2>Features & Usage</h2>
<p>There are four options on launch and one extra hidden option. Namely;
<ol>
<li> About Zac's Macbook Shop</li>
<li> See available models</li>
<li> Place Order</li>
<li> Exit</li>
</ol>
There is an extra option '0' that adds shipments to the database. As the app is still in beta testing, you can choose this for now to experiment with creating data functionality.
The other four options are interactive prompts to guide you through the app. Enjoy!
</p>

<h2>Languages</h3>
<p>The app is made uses python for the core logic, SQLAlchemy as the ORM and SQLite3 as the database. Alembic is used to handle migrations to the database and a record of all migrations can be found in the 'versions' directory. More modifications will continue to be added with time and any collaborators are welcome to add comments, suggestions to improve the app </p>


<h3>Licenses</h3>
<p>This App is licensed under the terms of the GPL Open Source license and is available for free.</p>




