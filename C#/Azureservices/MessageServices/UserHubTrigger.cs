using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Host;
using Microsoft.Azure.WebJobs.ServiceBus;

namespace Azureservices.MessageServices
{
    public static class UserHubTrigger
    {
        [FunctionName("UserHubTrigger")]
        public static void Run([EventHubTrigger("samples-workitems", Connection = "")]string myEventHubMessage, TraceWriter log)
        {
            log.Info($"C# Event Hub trigger function processed a message: {myEventHubMessage}");
        }
    }
}
