import { LicenseType } from "types/common/licenseType";
import { DefaultParams } from "types/api/common/params";
import { useMutation, useQueryClient } from "react-query";
import { DefaultAxiosService } from "types/defaultAxiosService";
import { ActivatedType } from "types/common/activatedType";

export interface CreateLicenseParams extends DefaultParams {
  sensors: Array<any>;
  allow_features: Array<any>;
  lidar_count: number;
  gpu_algo_node_count: number;
  algo_node_count: number;
  max_argos_session_count: number;
  name: string;
  machine_id: string;
  multiple: number;
  activated: ActivatedType;
  license_type: LicenseType;
  user: string;
  iat: string;
}

const createLicense = async (params: CreateLicenseParams) => {
  const url = `/license/`;
  const { data } = await DefaultAxiosService.instance.post(url, {
    sensors: params.sensors,
    allow_features: params.allow_features,
    lidar_count: params.lidar_count,
    gpu_algo_node_count: params.gpu_algo_node_count,
    algo_node_count: params.algo_node_count,
    max_argos_session_count: params.max_argos_session_count,
    name: params.name,
    machine_id: params.machine_id,
    multiple: params.multiple,
    activated: params.activated,
    license_type: params.license_type,
    user: params.user,
    iat: params.iat,
  });
  return data;
};

const useCreateLicense = () => {
  const queryClient = useQueryClient();
  return useMutation((params: CreateLicenseParams) => createLicense(params), {
    onMutate: (variables) => {},
    onSuccess: (res, variables, context) => {
      queryClient.invalidateQueries("read_license");
      queryClient.invalidateQueries("read_all_license");
      queryClient.invalidateQueries("read_license_summary");
      variables.successCallback && res && variables.successCallback(res);
    },
    onError: (err, variables, context) => {
      variables.errorCallback && err && variables.errorCallback(err);
    },
  });
};

export default useCreateLicense;