// The 'From' and 'To' fields are automatically populated with the values specified by the binding settings.
//
// You can also optionally configure the default From/To addresses globally via host.config, e.g.:
//
// {
//   "sendGrid": {
//      "to": "user@host.com",
//      "from": "Azure Functions <samples@functions.com>"
//   }
// }
using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Host;
using SendGrid.Helpers.Mail;

namespace Azureservices.Event
{
    public static class UserGrid
    {
        [FunctionName("UserGrid")]
        [return: SendGrid(ApiKey = "", To = "{CustomerEmail}", From = "SenderEmail@org.com")]
        public static Mail Run([QueueTrigger("sampleMessages", Connection = "")]Order order, TraceWriter log)
        {
            log.Info($"C# Queue trigger function processed order: {order.OrderId}");

            Mail message = new Mail()
            {
                Subject = $"Thanks for your order (#{order.OrderId})!"
            };

            Content content = new Content
            {
                Type = "text/plain",
                Value = $"{order.CustomerName}, your order ({order.OrderId}) is being processed!"
            };

            message.AddContent(content);
            return message;
        }
    }
    public class Order
    {
        public string OrderId { get; set; }
        public string CustomerName { get; set; }
        public string CustomerEmail { get; set; }
    }
}
