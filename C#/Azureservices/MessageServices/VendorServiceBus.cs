using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Host;
using Microsoft.ServiceBus.Messaging;

namespace Azureservices.MessageServices
{
    public static class VendorServiceBus
    {
        [FunctionName("VendorServiceBus")]
        public static void Run([ServiceBusTrigger("myqueue", AccessRights.Manage, Connection = "")]string myQueueItem, TraceWriter log)
        {
            log.Info($"C# ServiceBus queue trigger function processed message: {myQueueItem}");
        }
    }
}
