# Ticket Statuses

The following is a breakout of how HAUS labels and organizes tickets.

## Open

### `New`

A newly created ticket by a team member. 

### `Accepted`

Used to inform the team that the ticket is valid and is being worked on.

### `Reopened`

Used to inform the team that the ticket was reopened and requires additional attention. If you reopen a ticket, please add a comment explaining why it was reopened.

### `Waiting`

Signifies that the ticket cannot be acted upon and you need a response to continue work, i.e. you have questions regarding the ask, a creative asset is needed, etc. Please add a comment in which you describe the reason you cannot continue work. You should then reassign the ticket to the team member who can answer your question. If you're unsure who that is, reassign to the QA lead. If a QA lead hasn't been assigned or isn't onboard yet, you should assign it to the project manager.

### `WIP`

Signifies that you've made changes, but the ticket isn't finished yet. This can be because you need more time or the task requires work from another team member. If the latter, reassign to that team member, or add a comment in the ticket. 

**Note**: `WIP` labels should be used sparingly and only when absolutely necessary. Features and tasks should be focused and small enough to complete within a single day. If not, producers should consider splitting the ticket up into smaller tasks. 

### `Ready`

All changes for the ticket have been resolved and pushed to Git/Github – _but they have not been deployed to a test environment_. The ticket is "done", but not testable.

### `Test`

The changes for this ticket have been deployed to a test environment and can be tested by HAUS QA. Unless otherwise specified, this will be a standalone QA environment, i.e. http://honey-badger.qa.haus.la
 

## Closed

### `Invalid`

The issue described in this ticket is not correct. Please add a comment why this ticket is invalid.

### `Cannot Reproduce`

The issue described in this ticket is not reproducable.

### `Fixed`

The issue is resolved and approved by HAUS QA.

### `Won't Fix`

The issue described in this ticket is correct, but you aren't going to fix it. The issue may be out of scope, or there may be technical issues. Please add a comment as to why you won't fix the issue, and reassign back to the original author. 
