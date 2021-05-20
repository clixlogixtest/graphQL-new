import graphene

from graphene_django import DjangoObjectType, DjangoListField 
from .models import Business 


class BusinessType(DjangoObjectType): 
    class Meta:
        model = Business
        fields = "__all__"


class Query(graphene.ObjectType):
    all_business = graphene.List(BusinessType)
    business = graphene.Field(BusinessType, business_id=graphene.Int())

    def resolve_all_business(self, info, **kwargs):
        return Business.objects.all()

    def resolve_business(self, info, business_id):
        return Business.objects.get(pk=business_id)


class BusinessInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    address = graphene.String()
    owner_info = graphene.String()
    employee_size = graphene.Int() 

class CreateBusiness(graphene.Mutation):
    class Arguments:
        business_data = BusinessInput(required=True)

    business = graphene.Field(BusinessType)

    @staticmethod
    def mutate(root, info, business_data=None):
        business_instance = Business( 
            name=business_data.name,
            address=business_data.address,
            owner_info=business_data.owner_info,
            employee_size=business_data.employee_size
        )
        business_instance.save()
        return CreateBusiness(business=business_instance)

class UpdateBusiness(graphene.Mutation):
    class Arguments:
        business_data = BusinessInput(required=True)

    business = graphene.Field(BusinessType)

    @staticmethod
    def mutate(root, info, business_data=None):

        business_instance = Business.objects.get(pk=business_data.id)

        if business_instance:
            business_instance.name = business_data.name
            business_instance.address = business_data.address
            business_instance.owner_info = business_data.owner_info
            business_instance.employee_size = business_data.employee_size
            business_instance.save()

            return UpdateBusiness(business=business_instance)
        return UpdateBusiness(business=None)

class DeleteBusiness(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    business = graphene.Field(BusinessType)

    @staticmethod
    def mutate(root, info, id):
        business_instance = Business.objects.get(pk=id)
        business_instance.delete()
        return None

class Mutation(graphene.ObjectType):
    create_business = CreateBusiness.Field()
    update_business = UpdateBusiness.Field()
    delete_business = DeleteBusiness.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)