---
# User change
title: "Create a ASP.NET Core Web API project"

weight: 2

layout: "learningpathall"
---

## Introduction
ASP.NET Core is a cross-platform framework for building web applications that lets you develop web services as back ends for various scenarios. It also supports containerization, which you can use for building cloud-native applications. These characteristics and its cross-platform design make ASP.NET Core an ideal tool for building Internet of Things (IoT) web servers.

Windows 11 can run directly on Arm64-powered devices, so you can use it similarly to Windows 10 IoT Core to develop IoT apps. For example, you can use ASP.NET Core to build a web API that your headless IoT device exposes to communicate with users or other devices.

This Learning Path demonstrates how you can use ASP.NET Core with Windows 11 to build a web server for a headless IoT application and implement a temperature sensor emulator.

## Before you begin
Make sure that .NET is correctly installed on your machine. To do this, open the command prompt and type:

```console
dotnet --info
```

The output will show the list of installed SDKs. Make sure you have at least one SDK (ideally version 8 or above). 

{{% notice Note %}} Refer to this [learning path on .NET 8 applications on Windows on Arm](/learning-paths/laptops-and-desktops/win_net8/) for more details on the output of the dotnet --info command.{{% /notice %}}

## Create the project
You can now create a new ASP.NET Core Web API project. Open a command prompt window and type the following command:

```console
dotnet new webapi -o Arm64.HeadlessIoT
```

This command generates the output shown below:

```output
Welcome to .NET 8.0!
---------------------
SDK Version: 8.0.100

Telemetry
---------
The .NET tools collect usage data in order to help improve your experience. It is collected by Microsoft and shared with the community. You can opt-out of telemetry by setting the DOTNET_CLI_TELEMETRY_OPTOUT environment variable to '1' or 'true' using your favorite shell.

Read more about .NET CLI Tools telemetry: https://aka.ms/dotnet-cli-telemetry
----------------
Installed an ASP.NET Core HTTPS development certificate.
To trust the certificate, run 'dotnet dev-certs https --trust'
Learn about HTTPS: https://aka.ms/dotnet-https

----------------
Write your first app: https://aka.ms/dotnet-hello-world
Find out what's new: https://aka.ms/dotnet-whats-new
Explore documentation: https://aka.ms/dotnet-docs
Report issues and find source on GitHub: https://github.com/dotnet/core
Use 'dotnet --help' to see available commands or visit: https://aka.ms/dotnet-cli
--------------------------------------------------------------------------------------
The template "ASP.NET Core Web API" was created successfully.

Processing post-creation actions...
Restoring C:\Arm64.HeadlessIoT\Arm64.HeadlessIoT.csproj:
  Determining projects to restore...
  Restored C:\Arm64.HeadlessIoT\Arm64.HeadlessIoT.csproj (in 2.41 sec).
Restore succeeded.
```

The command creates a project containing a web API controller implemented in the `Controllers/WeatherForecastController.cs` file. This controller returns a collection of simulated weather forecasts. You do not need this controller and it can be removed by deleting the entire `WeatherForecastController.cs` file. The project is now ready and you can proceed with implementation.

## Implementation
In this section, you will learn how to implement the temperature sensor emulator, sensor service registration, and web API controller.

{{% notice Note %}} You can find the complete code in [this repository](https://github.com/dawidborycki/Arm64.HeadlessIoT). {{% /notice %}}

### Temperature Sensor Emulator
Start by implementing the temperature sensor emulator, which simulates readings from a temperature sensor connected to an IoT device running a web service.

To represent sensor readings, you can use the `SensorReading` class as defined in the code snippet below. To implement this class, create a Sensors folder in the Arm64.HeadlessIoT solution folder, then make a new file called **SensorReading.cs** where you place the following code:

```cs
namespace Arm64.HeadlessIoT.Sensors;
 
public class SensorReading 
{
    public double Value { get; private set; }
 
    public DateTime TimeStamp { get; }
 
    public SensorReading(double value)
    {
        Value = value;
        TimeStamp = DateTime.UtcNow;
    }
}
```

The class above contains two properties: **Value** and **TimeStamp**. The **Value** property stores the sensor reading while **TimeStamp** represents the time the reading was obtained. The SensorReading class also implements the constructor. You use this class to populate the Value property with the constructor parameter. The **TimeStamp** automatically provides the current date and time in UTC format.

Next, in the **Sensors** folder, create another file, **ISensor.cs**. Then modify the file as follows:

```cs
namespace Arm64.HeadlessIoT.Sensors;
 
public interface ISensor 
{
    public bool IsActive { get; set; }
 
    public SensorReading GetCurrentReading(); 
}
```

This interface provides a common contract for classes implementing sensor emulators. In this case, all the classes implementing the interface must implement the following two members:

1. `IsActive` — a Boolean property specifying whether the sensor is active and currently recording data
2. `GetCurrentReading` — a method returning an instance of the SensorReading class containing a sensor reading and timestamp

Now you can implement the actual class representing the temperature sensor. In the Sensors folder, add another file, **TemperatureSensor.cs**, which defines the following class:

```cs
namespace Arm64.HeadlessIoT.Sensors;
 
public class TemperatureSensor : ISensor
{
    private const int minValue = -10;
 
    private const int maxValue = 40;
 
    private SensorReading lastKnownReading 
        = new SensorReading(random.Next(minValue, maxValue));
 
    private static Random random = new();
 
    public bool IsActive {get; set;} = true;
    
    public SensorReading GetCurrentReading() 
    {
        if(IsActive)
        {
            var currentSensorReading = new SensorReading(random.Next(minValue, maxValue));
 
            lastKnownReading = currentSensorReading;
 
            return currentSensorReading;
        }
        else
        {
            return lastKnownReading;
        }
    }    
}
```

The `TemperatureSensor` class implements the **ISensor** interface, the `IsActive` property, and the `GetCurrentReading` method. The `IsActive` property is a Boolean value, which is initially **true**, indicating that the temperature sensor emulator is active.

The second method, `GetCurrentReading`, checks if the `IsActive` property is **true**. If so, the `GetCurrentReading` method simulates a temperature reading using a pseudo-random number generator (the `System.Random` class instance). Specifically, it uses the **Next** method of this generator to pick an integer value from a range of values stored in the min and max fields of the **TemperatureSensor** class. The `lastKnownReading` field stores the sensor reading. Finally, the `GetCurrentReading` method will return the temperature reading to the caller.

Alternatively, if the `IsActive` property is **false**, the `GetCurrentReading` method will return the last known sensor reading.

### Sensor Service Registration
After implementing the temperature emulator, use the dependency injection design pattern to register an instance of the **TemperatureSensor** as a singleton. To do this, you must modify the Program.cs file by adding using `Arm64.HeadlessIoT.Sensors` and `builder.Services.AddSingleton<ISensor, TemperatureSensor>()` as they appear below:

```cs
using Arm64.HeadlessIoT.Sensors;
 
var builder = WebApplication.CreateBuilder(args);
 
// Add services to the container.
builder.Services.AddControllers();

// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
 
builder.Services.AddSingleton<ISensor, TemperatureSensor>();
 
var app = builder.Build();
 
// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}
 
app.UseHttpsRedirection();
 
app.UseAuthorization();
 
app.MapControllers();
 
app.Run();
```

This approach ensures that a single instance of the TemperatureSensor class is available to the entire application. Any web API controller requiring access to that sensor can simply use the constructor injection.

You will also use the Swagger toolset. As shown above, the default ASP.NET Core Web API project template also registers two services, `EndpointsApiExplorer` and `SwaggerGen`:

```cs
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
```

You use these services to add Swagger middleware, which analyzes all the controllers in the project. It then generates a JSON-formatted file containing documentation of your web APIs and exposes the generated documentation on the HTTP endpoint using the following statements:

```cs
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}
```

### Web API Controller for the Headless IoT Device
Now you are ready to implement the web API controller. Create a new file **IoTController.cs** in the Controllers folder and add into it two using statements, defining the namespace as shown:

```cs
using Microsoft.AspNetCore.Mvc;
using Arm64.HeadlessIoT.Sensors;
 
namespace Arm64.HeadlessIoT.Controllers;
```

Next, define the `IoTController` class, which derives from the `ControllerBase` and contains the required controller attributes:

```cs
[ApiController]
[Route("[controller]")]
public class IoTController : ControllerBase
{
    
}
```

Then, in the `IoTController` class, define the read-only field, `temperatureSensor`, which stores the reference to the `TemperatureSensor` class instance registered in the dependency container in the Program.cs file:

```cs
private readonly ISensor temperatureSensor;
```

You can now define the `IoTController` class constructor:

```cs
public IoTController(ISensor sensor)
{
    temperatureSensor = sensor;
}
```

This code uses constructor dependency injection to obtain a reference to the `TemperatureSensor` class instance. The temperatureSensor field stores the reference to the `TemperatureSensor` class as defined in the Program.cs file.

Now, you can implement the `IoTController` method which handles GET requests:

```cs
[HttpGet]
[ProducesResponseType(typeof(SensorReading), StatusCodes.Status200OK)]
public SensorReading Get()
{
    return temperatureSensor.GetCurrentReading();
}
```

This method returns the temperature sensor emulator’s current reading.

Finally, implement the POST handler, which enables a user to change the sensor emulator’s `IsActive` property:

```cs
[HttpPost]
public IActionResult SetSensorStatus(bool isActive)
{
    temperatureSensor.IsActive = isActive;
 
    return Ok();
}
```

The final form of the **IoTController.cs** file is shown below:

```cs
using Microsoft.AspNetCore.Mvc;
using Arm64.HeadlessIoT.Sensors;

namespace Arm64.HeadlessIoT.Controllers;

[ApiController]
[Route("[controller]")]
public class IoTController : ControllerBase
{           
    private readonly ISensor temperatureSensor;

    public IoTController(ISensor sensor)
    {
        temperatureSensor = sensor;
    }

    [HttpGet]
    [ProducesResponseType(typeof(SensorReading), StatusCodes.Status200OK)]
    public SensorReading Get()
    {
        return temperatureSensor.GetCurrentReading();
    }

    [HttpPost]
    public IActionResult SetSensorStatus(bool isActive)
    {
        temperatureSensor.IsActive = isActive;

        return Ok();
    }
}
```

The implementation is ready and you can now build, run, and test the web server.
