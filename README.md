# Python-Assignment
<h1>Task 1 - Run a list of commands</h1>
<p>In commands, you are given a list of commands to execute. Use Popen to execute all commands at the same time.
When the execution of all commands are finished, display a report with, total elapsed time, average / maximum / minimum execution time among all commands.
Remember that processes started with Popen must be poll()'ed to make sure that they're finished and terminated properly.
commands list is:
commands = [
    'sleep 3',
    'ls -l /',
    'find /',
    'sleep 4',
    'find /usr',
    'date',
    'sleep 5',
    'uptime'
]</p>
<hr>
<h1>Task 2 - Send user data to Intercom</h1>
<p>We have a MySQL database that stores user information and the table spec for a simplified version of user is given below:

DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` text NOT NULL,
  `email` varchar(120) NOT NULL
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
Please write a simple script in Python that goes over our user database and creates users on Intercom.

You will need to use Intercom's API for this, but do not sign up for the service or use any real API keys for that. </p>
