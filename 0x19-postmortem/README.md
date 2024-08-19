# Postmortem: Outage of "Quiz Quest" Application
## Issue Summary
*Duration:* August 12, 2024, 14:00 - 16:30 UTC (2.5 hours)
Impact: The "Quiz Quest" application experienced a full outage, preventing 100% of users from accessing JAMB, WAEC, and aptitude practice questions. Users were met with a "Service Unavailable" error when trying to access the app, resulting in a complete loss of functionality during the outage.
Root Cause: The root cause was an exhausted database connection pool due to a configuration error in the connection pool settings, which caused all available connections to be consumed, leaving none for new user requests.

## Timeline
14:00 UTC: Issue detected via an automated monitoring alert indicating that the "Quiz Quest" application was down.
14:05 UTC: The engineering team was notified of the outage through the monitoring system.
14:10 UTC: Initial investigation focused on checking server status and network connectivity; no issues were found.
14:20 UTC: Assumptions were made that a recent deployment might have caused the issue, so the deployment logs were reviewed.
14:30 UTC: Misleading debugging path led to restarting the web servers, but the issue persisted.
14:45 UTC: The incident was escalated to the database team, as application logs indicated a possible database connectivity issue.
15:00 UTC: Database team identified that the connection pool was fully exhausted, causing new connection attempts to fail.
15:15 UTC: The team increased the connection pool size and restarted the application to resolve the issue.
15:30 UTC: The application was back online, and users were able to access the service.
16:00 UTC: A postmortem meeting was held to discuss the issue and determine preventive measures.
## Root Cause and Resolution
### Root Cause:
The root cause of the outage was a misconfiguration in the database connection pool settings. The connection pool was set to a maximum of 10 connections, which was insufficient given the increased traffic following a recent marketing campaign. As more users accessed the application, the connection pool quickly reached its limit, and all available connections were consumed. This left no connections available for new requests, resulting in a "Service Unavailable" error for all users.

### Resolution:
The issue was resolved by increasing the connection pool size to 50 connections, which provided enough capacity to handle the increased user load. The application was then restarted, allowing the changes to take effect, and restoring full functionality to the service. After monitoring the system for an additional hour, no further issues were observed, and the incident was deemed resolved.

Corrective and Preventative Measures
## Improvements/Fixes:

Increase Connection Pool Size: Ensure the connection pool size is appropriately configured to handle peak user load.
Load Testing: Perform regular load testing to simulate high-traffic scenarios and ensure the system can handle the expected number of users.
Monitoring Enhancements: Implement more granular monitoring of the database connection pool to detect and alert on high usage before it reaches a critical level.
### Tasks:

Patch Connection Pool Configuration: Update the connection pool configuration in the production environment to handle at least 50 connections.
*Add Connection Pool Monitoring:* Implement monitoring alerts for when the connection pool usage exceeds 80%.
*Conduct Load Testing:* Schedule a load testing session to ensure the new configuration can handle peak traffic.
Review Incident Response Procedure: Update the incident response playbook to include steps for quickly identifying and addressing database connection issues.
Deploy Monitoring Dashboards: Create and deploy dashboards to visualize connection pool usage in real-time for better monitoring.
By addressing these tasks, the likelihood of a similar issue occurring in the future will be significantly reduced.
