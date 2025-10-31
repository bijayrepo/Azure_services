using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Host;
using Microsoft.ServiceBus.Messaging;

namespace Azureservices.MessageServices
{
    public static class VendorServiceBusTopic
    {
        [FunctionName("VendorServiceBusTopic")]
        public static void Run([ServiceBusTrigger("mytopic", "mysubscription", AccessRights.Manage, Connection = "")]string mySbMsg, TraceWriter log)
        {
            log.Info($"C# ServiceBus topic trigger function processed message: {mySbMsg}");
        }
    }
}
