using System.IO;
using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Host;

namespace Azureservices.BlobTrigger
{
    public static class FileUploadManager
    {
        [FunctionName("FileUploadManager")]
        public static void Run([BlobTrigger("samples-workitems/{name}", Connection = "AzureWebJobsStorage")]Stream myBlob, string name, TraceWriter log)
        {
            log.Info($"C# Blob trigger function Processed blob\n Name:{name} \n Size: {myBlob.Length} Bytes");

            // Get BlobClient
            var blobServiceClient = BlobClientSingleton.Instance.GetBlobServiceClient();
            var containerClient = blobServiceClient.GetBlobContainerClient("images");
            var blobClient = containerClient.GetBlobClient(name);

            // Construct public URL
            string publicUrl = blobClient.Uri.ToString();
            log.Info($"Public URL: {publicUrl}");

        }
    }
}
