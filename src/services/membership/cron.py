from django_cron import CronJobBase, Schedule

from src.services.membership import check_and_send_expiration_notifications 

class MembershipExpirationCronJob(CronJobBase):
   
    schedule = Schedule(run_at_times=['00:00']) 
    code = 'src.services.membership.membership_expiration_cron'  

    def do(self):
        # Call the function that checks and sends expiration notifications
        check_and_send_expiration_notifications()
