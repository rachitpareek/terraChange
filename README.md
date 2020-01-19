# terraChange

terraChange aims to revolutionize the outdated bottle recycling system by integrating and gamifying the process for the end consumer. This app was built using flask, bootstrap, gcloud, & [a QR code generator](https://github.com/nayuki/QR-Code-generator). It is available live at `https://key-acre-265618.appspot.com`.


## Inherency

Hundreds of millions of tons of plastic, aluminum, and glass have gone to waste over the past decade as a result of ineffective recycling programs. These bottles can take from 700 years (in the case of plastic bottles) to 1 million (for glass bottles) to decompose. In California alone, [over $100 million worth of bottles and cans ended up in the waste](https://www.calrecycle.ca.gov/bevcontainer/consumers/facts). terraChange wants to put that money back in consumer's pockets while helping to decrease the massive amount of bottle waste created each year.

### Waste Creation

According to statista, 13.7 billion gallons of bottled water were sold across the US in 2017. This translates to the equivalent of roughly 103 billion 16.9 fluid ounce sized water bottles being consumed each year - just in the United States. Globally, this number increases, with the equivalent of 783 billion such water bottles being sold! This amounts to millions of tons of plastic waste, and unfortunately is not being recycled.

### Recycling effectiveness
Currently, approximately [1/3 of all plastic bottles](https://www.bottledwater.org/education/recycling) are recycled each year in the US, a rate that doubled over the past decade. Unfortunately, this rate remains low even though over 90% of American households have access to recycling programs. According to `bottledwater.org`:
- Of all the plastics produced in the United States, PET plastic bottled water packaging makes up only 0.92% -- less than one percent.
- Producing new products from rPET uses two-thirds less energy than required to make products from raw virgin materials. It also reduces greenhouse gas emissions
- Recycling a single plastic bottle can conserve enough energy to light a 60-watt light bulb for up to six hours

### Status Quo
California has one of the best recycling value programs in the US. States like Hawaii and Oregon also have well-established programs. These states would be ideal for initial program rollout, as our system promises to greatly increase adoption of the existing programs in these states.

In the current system, a consumer will pay an extra fee (called the "CRV" in California), which is then refunded to them if they recycle the bottles purchased. The point-of-sale (POS) and point-of-recycling both present pain points for the consumer, which terraChange's functionality addresses.

we use this for library books, loyalty programs, batteries (and all sorts of other hazardous waste). curr system is informal af and we can legitimize it. this gamifies the system and fits into exixsting workflow.  

## Functionality

terraChange is a web application that seamlessly integrates into the consumer's purchasing workflow and gamifies the recycling process. Existing systems such as tracking library books and other hazardous waste (like car batteries) already exist, signifying that a similar system is needed here. Furthermore, customers are used to scannign loyalty app's at the POS.

### Tracking
The process begins when the customer inputs the bottles to be recycled into the application. This can either be done  by conveniently scanning a personalized QR code at the POS or by manually inputting items into the application.

### Aggregating
The application keeps track of the items a customer has yet to recycle (and allows them to mark those they have recycled already). Their personal dashboard in the app will show how much recycling value they can take advantage of by recycling their outstanding items, gamifying the process.

### Recycling
Finally, the system will recommend to the consumer the closest recycling station based on total recycling value and open timings. This location can be accessed using the `Find Nearby Centers` tab in the application.

## Run with:
```Python
virtualenv ENV
source ENV/bin/activate
pip install -r requirements.txt
flask run
```
