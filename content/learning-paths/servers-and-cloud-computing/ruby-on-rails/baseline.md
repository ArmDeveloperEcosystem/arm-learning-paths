---
title: Ruby on Rails Baseline Testing on Google Axion C4A Arm Virtual Machine
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Baseline Setup for Ruby on Rails with PostgreSQL
This section sets up PostgreSQL and connects it with a Ruby on Rails application on a SUSE Arm64 Google Cloud C4A virtual machine. You’ll install PostgreSQL, configure it for Rails, create a database user, and verify that Rails can connect and serve requests successfully.

### Install and Configure PostgreSQL
PostgreSQL is a robust, production-grade relational database that integrates seamlessly with Ruby on Rails.

Install PostgreSQL and its development headers:

```console
sudo zypper install postgresql-devel postgresql-server
```
- `postgresql-devel` is required to compile the pg gem for Rails.

After installation, ensure that PostgreSQL is running and configured to start automatically at boot:

```console
sudo systemctl start postgresql
sudo systemctl enable postgresql
systemctl status postgresql
```
The output should look like:
```output
● postgresql.service - PostgreSQL database server
     Loaded: loaded (/usr/lib/systemd/system/postgresql.service; enabled; vendor preset: disabled)
     Active: active (running) since Tue 2025-11-04 21:25:59 UTC; 18s ago
   Main PID: 26997 (postgres)
      Tasks: 7
        CPU: 372ms
     CGroup: /system.slice/postgresql.service
             ├─ 26997 /usr/lib/postgresql15/bin/postgres -D /var/lib/pgsql/data
             ├─ 26998 "postgres: logger " "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "">
             ├─ 26999 "postgres: checkpointer " "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "">
             ├─ 27000 "postgres: background writer " "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" >
             ├─ 27002 "postgres: walwriter " "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "">
             ├─ 27003 "postgres: autovacuum launcher " "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ">
             └─ 27004 "postgres: logical replication launcher " "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ">
```
If the Active state reads running, your PostgreSQL service is operational and ready for configuration.

### Create a Database Role for Rails
Next, create a dedicated PostgreSQL role (user) that Rails will use to connect to the database.

```console
sudo -u postgres psql -c "CREATE USER gcpuser WITH SUPERUSER PASSWORD 'your_password';"
```
This command:

Executes under the default PostgreSQL superuser account (postgres).
Creates a new PostgreSQL role called gcpuser.
Assigns superuser privileges, allowing the user to create databases, manage roles, and execute administrative tasks.

This user will serve as the Rails database owner and be referenced in the Rails configuration file (config/database.yml) later.

### Set Environment variables

Before creating your Rails application, export environment variables so Rails and the `pg gem` can authenticate automatically with PostgreSQL.

```console
export PGUSER=gcpuser
export PGPASSWORD=your_password
export PGHOST=localhost
```

PGUSER → Specifies the PostgreSQL user that Rails will connect as.
PGPASSWORD → Stores the password for that user in memory (temporary for this session).
PGHOST → Points to the PostgreSQL host (in this case, the local VM).

### Create a Rails App with PostgreSQL
Now, generate a new Rails application configured to use PostgreSQL as its default database adapter:

```console
rails new db_test_rubyapp -d postgresql
cd db_test_rubyapp
bundle install
```
- rails new db_test_rubyapp → Creates a new Rails application named db_test_rubyapp.
- `d postgresql` → Instructs Rails to use PostgreSQL instead of the default SQLite database.
- bundle install → Installs all gem dependencies defined in the Gemfile, including the pg gem that connects Rails to PostgreSQL.

{{% notice Note %}}
Check `config/database.yml` to ensure the `username` and `password` match your PostgreSQL role `(gcpuser)`.
{{% /notice %}}

### Verify and Update Database Configuration
Rails uses the `config/database.yml` file to define how it connects to databases in different environments (development, test, and production).
It's important to verify that these credentials align with the PostgreSQL role you created earlier.

Open the file with your preferred text editor:

```console
sudo vi config/database.yml
```
Locate the default and development sections, and make sure they match the PostgreSQL user and password you configured.

Your configuration file should have the following fields set:
```output
default: &default
  adapter: postgresql
  encoding: unicode
  username: gcpuser
  password: your_password
  host: localhost
  pool: 5

development:
  <<: *default
```

### Change the Authentication Method
By default, PostgreSQL on many Linux distributions (including SUSE) uses the ident authentication method for local connections. This method maps Linux system usernames directly to PostgreSQL roles. While convenient for local access, it prevents password-based authentication, which is necessary for Rails and most application connections.

To allow Rails to connect using a username and password, change the authentication method in PostgreSQL’s configuration file `pg_hba.conf` from ident to md5.

Open your configuration file
```console
sudo vi /var/lib/pgsql/data/pg_hba.conf
```
The file location `/var/lib/pgsql/data/pg_hba.conf` is the default data directory path for PostgreSQL on SUSE Linux.

Find lines like the following in the file:

```output
# IPv4 local connections:
host    all             all             127.0.0.1/32            ident
# IPv6 local connections:
host    all             all             ::1/128                 ident
```
Modify both lines to use md5, which enables password-based authentication:

```output
# IPv4 local connections:
host    all             all             127.0.0.1/32            md5
# IPv6 local connections:
host    all             all             ::1/128                 md5
```
After saving the file, restart the PostgreSQL service to apply the new authentication settings:

```console
sudo systemctl restart postgresql
```

Verify the change:
```console
sudo systemctl status postgresql
```
The service should show as active (running).

### Create and Initialize the Database
Once PostgreSQL is configured and Rails can authenticate, you can create your application’s development and test databases.
This step verifies that Rails is correctly connected to PostgreSQL and that the pg gem is working on your Arm64 environment.

Run the following command from inside your Rails app directory:
```console
rails db:create
```
You should see output similar to:
```output
Created database 'db_test_rubyapp_development'
Created database 'db_test_rubyapp_test'
```
This output confirms that Rails successfully. It connected to the PostgreSQL service using the credentials from `config/database.yml` and created two new databases — one for development and one for testing.

### Generate a Scaffold for Testing
To verify your Ruby on Rails and PostgreSQL integration, you’ll create a small scaffold application.
A scaffold is a Rails generator that automatically builds a model, controller, views, and database migration, allowing you to test CRUD (Create, Read, Update, Delete) operations quickly.

For this example, you’ll create a simple Task Tracker app that manages tasks with titles and due dates.
Run the following command inside your Rails project directory:

```console
rails generate scaffold task title:string due_date:date
```
This single command automatically generates:
A database migration to create the tasks table in PostgreSQL.
A model file (app/models/task.rb) that maps to the tasks table.
A controller (app/controllers/tasks_controller.rb) with full CRUD actions (index, show, new, create, edit, update, destroy).
Corresponding views in app/views/tasks/ with ready-to-use HTML + embedded Ruby templates.
Route entries in config/routes.rb to make the new resource accessible via /tasks.

Now apply the migration to create the tasks table in your PostgreSQL database:

```console
rails db:migrate
```

You should see output similar to:
```output
== 20251006101717 CreateTasks: migrating ======================================
-- create_table(:tasks)
   -> 0.0127s
== 20251006101717 CreateTasks: migrated (0.0128s) =============================
```

This confirms that Rails connected successfully to PostgreSQL and the database schema was updated.
The new tasks table was created inside your db_test_rubyapp_development database.

### Verify Table and Database Connectivity
TThe scaffold created a tasks table in your PostgreSQL database. Verify it exists and has the expected schema:

```console
sudo -u postgres psql
```
Inside the PostgreSQL shell, run:

```console
\c db_test_rubyapp_development
\d tasks
\q
```
- `sudo -u postgres psql` → Launches the PostgreSQL shell as the superuser `postgres`.
- `\c db_test_rubyapp_development` → Connects to the Rails app’s development database.
- `\d tasks` → Displays the schema (columns and types) of the `tasks` table.
- `\q → Exit from the PostgreSQL shell
  
You should see output similar to:
```output
psql (15.10)
Type "help" for help.

postgres=# \c db_test_rubyapp_development
You are now connected to database "db_test_rubyapp_development" as user "postgres".
db_test_rubyapp_development=# \d tasks
                                          Table "public.tasks"
   Column   |              Type              | Collation | Nullable |              Default
------------+--------------------------------+-----------+----------+-----------------------------------
 id         | bigint                         |           | not null | nextval('tasks_id_seq'::regclass)
 title      | character varying              |           |          |
 due_date   | date                           |           |          |
 created_at | timestamp(6) without time zone |           | not null |
 updated_at | timestamp(6) without time zone |           | not null |
Indexes:
    "tasks_pkey" PRIMARY KEY, btree (id)
```

### Open port 3000 in Google Cloud (VPC firewall)
Before proceeding to run the Rails server, you need to allow port 3000 from your GCP console. Below are the steps to do that:

a. On the GCP console, navigate to **Firewall** -> **Create Firewall Rule**
 
 ![Firewall Info alt-text#center](images/firewall1.png "Figure 1: Firewall Create")

b. Fill in the details as below:

Give a **name** for your desired port (e.g., `allow-3000-ingress`).

![Allow Ingress alt-text#center](images/firewall2.png "Figure 2: Allow-3000-ingress ")
 

Set **Direction of Traffic** to **"Ingress"**.

Set **Target** to **"All Instances in the Network"**. You can also choose **"Specific Tags"**.

Set the **Source IPv4 range** to **"0.0.0.0/0"**, for global access.

![Set Direction of Traffic  alt-text#center](images/firewall3.png "Figure 3: Target Set")
 
In the **"Protocols and Ports"**, click on **"TCP"**, and mention the port number **"3000"**.
 
![Set Protocols and Ports  alt-text#center](images/firewall4.png "Figure 4: Protocols and Ports")
 
 
Click on **"Create"**. The Firewall rule will be created successfully and can be viewed in the Firewall Policies Page:

![ Create Firewall rule alt-text#center](images/firewall5.png "Figure 5: Create Firewall rule")

 ### OS firewall (firewalld) on SUSE
Once done, go back to your VM, install FirewallD:
```console
sudo zypper install firewalld
```
Now start FirewallD and execute the commands to allow port 3000:
 
```console
sudo systemctl start firewalld
sudo systemctl enable firewalld
sudo firewall-cmd --permanent --add-port=3000/tcp
sudo firewall-cmd --reload
```

## Start Rails
Now that port 3000 is allowed in your VM’s ingress firewall rules, you can start the Rails server using the following command:

```console
rails server -b 0.0.0.0
```
- `rails server -b 0.0.0.0` → Starts the Rails server and binds it to all network interfaces, not just `localhost`.
- Binding to `0.0.0.0` allows other machines (or your local browser) to access the Rails app running on the VM using its external IP.


### Access the Application:
Open a web browser on your local machine (Chrome, Firefox, Edge, etc.) and enter the following URL in the address bar:

```console
http://[YOUR_VM_EXTERNAL_IP]:3000
```
- Replace `<YOUR_VM_PUBLIC_IP>` with the public IP of your GCP VM.

You will see a Rails welcome page in your browser if everything is set up correctly. It looks like this:

![Rails-info page alt-text#center](images/rails-web.png "Figure 6: Ruby/Rails Welcome Page")

With port 3000 reachable and the welcome page loading, your Rails stack on SUSE Arm64 (C4A Axion) is verified end-to-end and you can proceed to benchmarking.
