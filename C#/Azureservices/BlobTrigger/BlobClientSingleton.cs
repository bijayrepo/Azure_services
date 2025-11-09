using Azure.Storage.Blobs;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Azureservices.BlobTrigger
{
    internal sealed class BlobClientSingleton
    {
        private static readonly Lazy<BlobClientSingleton> instance =
        new Lazy<BlobClientSingleton>(() => new BlobClientSingleton());

        private readonly BlobServiceClient blobServiceClient;

        private BlobClientSingleton()
        {
            string blobConnectionString = Environment.GetEnvironmentVariable("AzureWebJobsStorage");
            blobServiceClient = new BlobServiceClient(blobConnectionString);
        }

        public static BlobClientSingleton Instance => instance.Value;

        public BlobServiceClient GetBlobServiceClient()
        {
            return blobServiceClient;
        }

    }
}
